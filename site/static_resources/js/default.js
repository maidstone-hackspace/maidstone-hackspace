$(document).ready(function(){
    $('.ajaxPopup, .ajax-form').on('click', function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr('href'),
            context: document.body
        }).done(function(html) {
            $( this ).addClass( "done" );
            $('#ajaxPopup > div.content').html(html);
            $('#ajaxPopup').show();
        });
        
    });
    $('.closePopup').on('click', function(e){
        e.preventDefault();
        $('#ajaxPopup').hide();
    });
});
