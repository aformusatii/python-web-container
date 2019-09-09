import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import imp
import os

from tornado.options import define, options

handlers = list()
webapp_config = {}

for r, d, f in os.walk('../webapps'):
    for file in f:
        if file.endswith('.py'):
            print('Loading python file: [{}]'.format(os.path.join(r, file)))
            webapp = imp.load_source('webapp', os.path.join(r, file))
            
            if "add_handlers" in dir(webapp):
                webapp.add_handlers(handlers)
                
            if "configure" in dir(webapp):
                key = r.split(os.path.sep)[-1]
                webapp_config[key] = {}
                webapp.configure(webapp_config[key])


define("port", default=8981, help="run on the given port", type=int)

class NoCacheStaticFileHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        # Disable cache
        self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')


for o in os.listdir('../webapps'):
    if str(o) in webapp_config:
        http_path = webapp_config[o]["path"]
    else:
        http_path = "/{}".format(o)
        
    print("Register static resources for: [{}] under path: [{}]".format(o, http_path))
    
    if http_path == "/":
        handlers.append((r"{}".format(http_path), tornado.web.RedirectHandler, {"url": "{}index.html".format(http_path)}))
        handlers.append((r"{}(.*)".format(http_path), NoCacheStaticFileHandler, {"path": "../webapps/{}/static".format(o)}))
    else:    
        handlers.append((r"{}".format(http_path), tornado.web.RedirectHandler, {"url": "{}/index.html".format(http_path)}))
        handlers.append((r"{}/".format(http_path), tornado.web.RedirectHandler, {"url": "{}/index.html".format(http_path)}))
        handlers.append((r"{}/(.*)".format(http_path), NoCacheStaticFileHandler, {"path": "../webapps/{}/static".format(o)}))

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(handlers, autoreload=True)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()