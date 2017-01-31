(function($){   
    $(function(){
        $(document).ready(function() {
            $('#id_componente').bind('change', rango_change);           
            $('#id_rango >option').show();
        });
});  
})(django.jQuery);

// based on the type, action will be loaded

var $ = django.jQuery.noConflict();

function rango_change()
{
    var action_type = $('#id_type').val();
    $.ajax({
            "type"     : "GET",
            "url"      : "/choices/?rango_type="+action_type,
            "dataType" : "json",
            "cache"    : false,
            "success"  : function(json) {
                $('#id_rango >option').remove();
                for(var j = 0; j < json.length; j++){
                    $('#id_rango').append($('<option></option>').val(json[j][0]).html(json[j][1]));
                }
            }           
    })(jQuery);
}