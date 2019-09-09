var app = null;

(function(angular) {
    'use strict';
    app = angular.module('ngHomePortal', ['ngRoute']);
    app
        .controller('NavBarController', NavBarController)

        .config(function($routeProvider, $locationProvider) {
            // see https://docs.angularjs.org/api/ngRoute/service/$route#examples
            $routeProvider
                .when('/environment', {
                    templateUrl: 'body/services.html'
                })
                .when('/service-descriptors', {
                    templateUrl: 'body/service-descriptors.html'
                });
        });

})(window.angular);

var addRoute = function(path, file) {
    app.config(function($routeProvider, $locationProvider) {
        $routeProvider.when(path, {templateUrl: file});
    });
}