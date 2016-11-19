$(document).ready(function() {
   	$('div.switch span i').hide();
   	setInterval(function(){getStates();}, 500);
   	$('div.switch').on('click', function() {
    	$(this).children('span').children('i').show();
    	$.get('/lights/change_state/', {sourceId: $(this).attr('data-id')}, function(data){
         	
        });
    	
    });

    function getStates () {
    	$.get('/lights/check_sources/', {}, function(data){
            $.each(data, function (index, object) {
            	$('div.switch span i').hide();
            	if (object.fields.current_state == 0) {
            		$('div.switch[data-id="'+object.pk+'"]').removeClass('enabled disabled').addClass('disabled');
            	}
            	else {
            		$('div.switch[data-id="'+object.pk+'"]').removeClass('enabled disabled').addClass('enabled');
            	}
            });
        });
    }


});