/**
 * Created by samuelraker on 1/27/14.
 */
$(document).ready(function () {
    'use strict';
    var index = 1, $form_groups = $(".fg"),
        form_groups_length = $form_groups.length,
        $buttons = $("#buttons"), i, j, hide_all, show_next, other_stuff;
    $buttons.hide();
    hide_all = function() {
        for (i = 2; i <= form_groups_length; i++) {
            $("#"+i).hide();
        }
    };
    show_next = function () {
        var fg_index = index;
        $("#"+fg_index).hide("slide", {direction: "up"}, 500);
        if ((fg_index + 1) <= form_groups_length) {
            $("#"+(fg_index + 1)).show("slide", {direction: "down"}, 500);
        }
        else {
            $buttons.show("slide", {direction: "down"}, 500);
        }
        index++;
    };

    hide_all();
    for (j = 1; j <= form_groups_length; j++) {
        $("button#next-" + j).on('click', show_next);
    }

    $("h2").off();
    $(".grey").off();
    $("#about-parent").on("click", ".h2", function() {
        var ok = window.confirm("Your progress will be lost!\nReally leave the survey?");
        if (ok === true) {
            document.stuff.load_about();
        }
    });
    $("#cv-parent").on("click", ".h2", function() {
        var ok = window.confirm("Your progress will be lost!\nReally leave the survey?");
        if (ok === true) {
            document.stuff.load_cv();
        }
    });

    other_stuff = {
        "hide_all": hide_all,
        "show_next": show_next
    };
    $.extend(document.stuff, other_stuff);
});