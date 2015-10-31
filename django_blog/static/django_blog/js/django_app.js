var host = location.protocol.concat("//").concat(window.location.hostname).concat(":").concat(window.location.port);
var postIdForDelete=0;
var app = angular.module('django_blog', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('blogCtrl', function($scope, $http){

    $http.get(host + "/api/posts/").success(function(response){
        $scope.all_post = response;
    });

    $scope.update = function(id){
        window.location = host + "/blog/" + id + "/update";
    }

    $scope.confirm = function(id){
        postIdForDelete = id;
        $('#myModal').modal('show');
    }

    $scope.deletePost = function(){
        window.location = host + "/blog/" + postIdForDelete + "/delete";
    }

    $scope.postDetails = function(id){
        window.location = host + "/blog/post/" + id;
    }

    $scope.shortText = function(content){
        var maxLength = 300; // maximum number of characters to extract
        //trim the string to the maximum length
        var trimmedString = content.substr(0, maxLength);
        //re-trim if we are in the middle of a word
        trimmedString = trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" ")));
        return trimmedString + " ... ";
    }
});
