// 'IIFE' Immediatly Invoked Function Expression 
//is a function which will call itself

(function(){
    'use strict';
    angular.module('scrumboard.demo',[])
    .controller('ScrumboardController', ['$scope','$http', ScrumboardController]);

    function ScrumboardController($scope, $http) {
        $scope.add_to_cards = function(list, new_card) {
            var card = {
                title : new_card
            };

            list.cards.push(card);
        };

        $scope.data = [];
        $http.get('/scrumboard/alllist').then(function(response) {
            $scope.data = response.data;
        });
       
    }
}());