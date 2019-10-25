    
$(function(){

    var conditional_fields = $(".form-row.field-duration_type");
    
    if ($("#id_max_duration").val().length == 0) {
        conditional_fields.hide();
    }

    $("#id_max_duration.vIntegerField").on('change keyup', function() {
        if ($(this).val().length == 0 || $(this).val() == 0 ) {
            $("#id_duration_type").prop('selectedIndex', 0);
            conditional_fields.slideUp(700);
        } else {
            conditional_fields.slideDown(700);
        }
    });

});


