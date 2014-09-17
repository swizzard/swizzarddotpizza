$(document).ready(function () {
    'use strict';
    var do_mail, load_about, load_cv, load_survey, load_vst, close_cv, close_about, close_survey, close_vst, close_all, stuff;
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
        return false;
    };
    close_vst = function () {
      $("#vst-parent").html("<h2 id='vst'>Very Silly Things&reg;</h2>");
      return false;
    };
    close_all = function () {
      close_about();
      close_cv();
      // close_survey();
      close_vst();
      return false;
    };
    load_about = function () {
        $("#about-parent").load("/load_etc/");
        close_vst();
        // close_survey();
        close_vst();
        $("#about-parent").on('click', '.grey', close_about);
        return false;
    };
    load_cv = function () {
        $("#cv-parent").load("/load_cv/");
        close_about();
        // close_survey();
        close_vst();
        $("#cv-parent").on('click', '.grey', close_cv);
        return false;
    };
    load_survey = function () {
        $("#survey-parent").load("/hash_to_hash/");
        close_about();
        close_cv();
        close_vst();
        $("#survey-parent").on('click', '.grey', close_survey);
        return false;
    };
    load_vst = function () {
      $("#vst-parent").load("/load_vst/");
      close_about();
      close_cv();
      // close_survey();
      $("#vst-parent").on('click', '.grey', close_vst);
    };


    $("#about-parent").on('click', 'h2', load_about);
    $("#cv-parent").on('click', 'h2', load_cv);
    $("#survey-parent").on('click', 'h2', load_survey);
    $("#vst-parent").on('click', 'h2', load_vst);
    $("h1").on('click', close_all);

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
        "close_all": close_all
    };
    document.stuff = stuff;
});
