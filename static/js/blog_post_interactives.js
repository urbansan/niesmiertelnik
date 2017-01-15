$(document).ready(function(){
	var start_width = $("#blog_content").width();
	var start_height = start_width * 0.5;
	$("iframe").width(start_width);
	$("iframe").height(start_height);

	$(window).resize(function(){
		var changed_width = $("#blog_content").width();
		$("iframe").width(changed_width);
		$("iframe").height(changed_width * 0.5);
	});

});