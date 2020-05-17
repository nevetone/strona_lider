
$(document).ready(function(){
    var loading_screen = $('.loading_screen');
    loading_screen.remove();

    $(".content").animate({
        opacity : 1
    }, 500);

    if ($(window).width() > 991){
        $('.navbar-dark .d-menu').hover(function () {
                $(this).find('.sm-menu').first().stop(true, true).slideDown(150);
            }, function () {
                $(this).find('.sm-menu').first().stop(true, true).delay(120).slideUp(100);
            });
            }

        $('#mceu_30').css('width', 'auto');
    
});