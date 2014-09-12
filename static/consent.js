/**
 * Created by samuelraker on 1/29/14.
 */
$(document).ready(function(){'use strict';
    var $survey = $("#survey-parent");
    $("#consent").on("click", function() {
            var r = window.confirm("I have read this consent form and agree to the terms.");
            if (r === true) {
                 $survey.load("/hash/start/");
            } else {
                document.stuff.close_survey();
            }
        });
    $("#no").on("click", document.stuff.close_survey
    );
});