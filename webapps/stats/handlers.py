import tornado.web

def add_handlers(handlers):
    handlers.append((r"/api/stats", StatsHandler))
    
def read_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

class StatsHandler(tornado.web.RequestHandler):
    def get(self):
        
        body = read_content('/sys/class/thermal/thermal_zone0/temp')
        body = body + read_content('/proc/meminfo')
        body = body + read_content('/proc/stat')
        
        body = body + 'Test 3'
        
        self.write(body)