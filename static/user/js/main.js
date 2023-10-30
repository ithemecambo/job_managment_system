$(document).ready(function(){
	$(window).bind('scroll', function() {
	   	var navHeight = $( window ).height() - 80;
			if ($(window).scrollTop() > navHeight) {
				$('.navbar').addClass('fixed');
			} else {
				$('.navbar').removeClass('fixed');
			}
	});
});