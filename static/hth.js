(function() {'use strict';
	$(document).ready(function () {
		$(".context").slideUp();
		$("input[id^=context]").on('click', function() {
			var tag = $(this).attr('id').split("-")[1];
			if (tag === "tag1") {
				$(".context.1").slideDown();
			}
			else if (tag === "tag2") {
				$(".context.2").show();
			}
		});
		$("#consent").on("click", function(e) {
            var r = window.confirm("I have read this consent form and agree to the terms.");
            if (r === true) {
                 $("#hth").load("/hash/start");
            } else {
                window.location.href = "/";
            }
            return false;
        });
        $("#no").on("click", function() {
          window.location.href = "/";
        });
        $('input[type="submit"]').on('click', function() {
            $(".row.form-action").load("{{ action }}");
        });
    });
})();
