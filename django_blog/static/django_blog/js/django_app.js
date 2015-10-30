var app = angular.module('django_blog', []);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller('blogCtrl', function($scope, $http){
    $http.get("http://www.w3schools.com/angular/customers.php")
    .success(function(response){
        $scope.all_post = response.records;
    });
});