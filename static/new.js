$(document).ready(function () {
    'use strict';
    var do_mail, load_about, load_cv, load_survey, load_vst, close_cv, close_about, close_survey, close_vst, stuff;
    do_mail = function () {
        $(".mail").html('<a href="mailto:' + ['sa', 'm.r', 'ak', 'er@', 'gm', 'ai', 'l.c', 'om'].join('') + '">Sam Raker</a>');
    };
    do_mail();
        close_about = function () {
        $("#about-parent").html("<h2 id='about'>About</h2>");
        return false;
    };
    close_cv = function () {
        $("#cv-parent").html("<h2 id='cv'>CV</h2>");
        return false;
    };

    close_survey = function () {
        $("#survey-parent").html("<h2>Survey</h2>");
    };
    close_vst = function () {
      $("#vst-parent").html("<h2>Very Silly Things&reg;</h2>");
    };
    load_about = function () {
        $("#about-parent").load("/load_etc/");
        $("#cv-parent").html("<h2 id='cv'>CV</h2>");
        $("#survey-parent").html("<h2 id='survey'>Survey</h2>");
        $("#about-parent").on('click', '.grey', close_about);
        return false;
    };
    load_cv = function () {
        $("#cv-parent").load("/load_cv/");
        $("#about-parent").html("<h2 id='about'>About</h2>");
        $("#survey-parent").html("<h2 id='survey'>Survey</h2>");
        $("#cv-parent").on('click', '.grey', close_cv);
        return false;
    };
    load_survey = function () {
        $("#survey-parent").load("/hash_to_hash/");
        $("#about-parent").html("<h2 id='about'>About</h2>");
        $("#cv-parent").html("<h2 id='cv'>CV</h2>");
        $("#survey-parent").on('click', '.grey', close_survey);
        return false;
    };
    load_vst = function () {
      $("#vst-parent").load("/load_vst/");
      $("#about-parent").html("<h2 id='about'>About</h2>");
      $("#cv-parent").html("<h2 id='cv'>CV</h2>");
      $("#vst-parent").on('click', '.grey', close_vst);
    };

    $("#about-parent").on('click', 'h2', load_about);
    $("#cv-parent").on('click', 'h2', load_cv);
    $("#survey-parent").on('click', 'h2', load_survey);
    $("#vst-parent").on('click', 'h2', load_vst);


    switch(window.location.pathname) {
      case "/about/":
        load_about();
        break;
      case "/etc/":
        load_about();
        break;
      case "/cv/":
        load_cv();
        break;
      case "/survey/":
        load_survey();
        break;
      case "/vst/":
        load_vst();
        break;
    }

    stuff = {
        "do_mail": do_mail,
        "load_about": load_about,
        "load_cv": load_cv,
        "load_survey": load_survey,
        "close_about": close_about,
        "close_cv": close_cv,
        "close_survey": close_survey,
        "load_vst": load_vst,
        "close_vst": close_vst,
    };
    document.stuff = stuff;
});
