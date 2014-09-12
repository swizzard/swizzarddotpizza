(function () {'use strict';
    $(document).ready(function () {
        $('.mail-to').prop('href',function() {var a = ['ma','ilt','o:','sa','m.r','ak','er','@g','ma','il.','com']; return a.join('');});
        $(".to-hide h3").siblings().hide();
        $(".to-hide h3").mouseover(function() {
            $(this).siblings().show();
        });
        $(".to-hide").mouseleave(function() {
            $(this).children().filter(":eq(0)").siblings().hide();
        });
        $("#consent").bind("click", function() {
            var r = window.confirm("I have read this consent form and agree to the terms.");
            if (r === true) {
                window.location.href = "/hash/start";
            } else {
                window.location.href = "/";
            }
        });
        $("#no").bind("click", function() {
          window.location.href = "/";
        });
    });
    }());
