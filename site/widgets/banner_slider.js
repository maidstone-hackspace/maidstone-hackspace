var app = angular.module('myApp', ['ngAnimate']);

app.controller('sliderController', function($scope, $interval) {
    $scope.currentSlide = 0;
    $scope.autoSlide = true;
    //$scope.length = 0;

    $scope.next = function() {
        $scope.autoSlide=false;
        if ($scope.currentSlide < $scope.length - 1){
            $scope.currentSlide += 1;
        }else{
            $scope.currentSlide = 0;
        };
    }

    $scope.prev = function() {
        $scope.autoSlide=false;
        if ($scope.currentSlide > 0){
            $scope.currentSlide -= 1;
        }else{
            $scope.currentSlide = $scope.length - 1;
        }
    }

    $scope.isCurrentSlideIndex = function (index) {
        return $scope.currentSlide === index;
    };

    $scope.loopSlides = function (index) {
        if ($scope.autoSlide==false){return false;}
        if ($scope.currentSlide < $scope.length - 1){
            $scope.currentSlide += 1;
        }else{
            $scope.currentSlide = 0;
        }
    };

    $interval(function(){$scope.loopSlides();}, 5000);

});
