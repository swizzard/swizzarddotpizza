/**
 * Created by samuelraker on 1/29/14.
 */
$(document).ready(function() {'use strict';
    var $survey = $("#survey-parent");
    $("button#intro-ok").on('click', function() {
        $survey.load("/hash/survey/");
    });
    document.stuff.do_mail();
});