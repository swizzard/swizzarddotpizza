var ffy = function(){
    'use strict';
     $('document').ready(function() {
        var showSelectedTeam = function() {
            $('.tradeform').hide();
            var otherTeamName = $("#otherteams option:selected").text();
            $("#tradeform-" + otherTeamName).show();
            };
        $("#otherteams").change(showSelectedTeam);
        showSelectedTeam();
        $("#signout").on('click', function() {window.location.replace("http://www.samraker.com/ffy/signout/");});
        $("#dont").on('click', function() {window.location.href("http://www.samraker.com/ffy/overview/");});
        $(".key").hide();
//         var i = 0;
        $(".show-key").on('click', function() {
            $(".key").slideToggle();
            // i++;
//             if (i%2 === 1) {
//                 $(".key").slideDown();
//                 }
//             else {
//                 $(".key").slideUp();
//                 }
            });
        });
    };
$("document").ready(ffy());
