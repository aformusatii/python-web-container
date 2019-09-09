var NavBarController = function($rootScope, $scope, $route, $routeParams, $location, $rootScope, $http) {
    $scope.params = $routeParams;
    $scope.$location = $location;
}

var addNavItem = function(name, path) {
    app.run(['$rootScope', function($rootScope){
        $rootScope.navItems = [];
        $rootScope.navItems.push({
            name: name,
            path: path
        });  
    }]);
}