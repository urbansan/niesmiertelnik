$(document).ready(function(){

	var top_offset = $("nav").offset().top;
	$("nav.navbar").wrap('<div class="sticky-placeholder"></div>');
	$(".sticky-placeholder").height($("nav.navbar").outerHeight());

	$(window).scroll(function(){
		if($(window).width() > 750){
			var scroll_position = $(window).scrollTop();

			if(scroll_position >= top_offset){
				$("nav.navbar").addClass("sticky");
			} else {
				$("nav.navbar").removeClass("sticky");
			}
		} else {
			$("nav.navbar").removeClass("sticky");
		}
	});

	var side_offset = $("#boczniaczek").offset().top - $("nav.navbar").outerHeight();
	var side_width = $("#boczniaczek").width();
	$("#boczniaczek").wrap('<div class="boczniaczek-placeholder"></div>');
	$(".boczniaczek-placeholder").height($("#boczniaczek").outerHeight());

	$(window).scroll(function(){
		var scroll_position = $(window).scrollTop();
		if($(window).width() > 750){
			if(scroll_position >= side_offset){
				$("#boczniaczek").addClass("boczny");
				$("#boczniaczek").css("top", $("nav.navbar").outerHeight());
				$("#boczniaczek").width(side_width);
			} else {
				$("#boczniaczek").removeClass("boczny");
				$("#boczniaczek").css("top", "auto");
			}
		} else {
				$("#boczniaczek").removeClass("boczny");
				$("#boczniaczek").css("top", "auto");
			}
	});



});