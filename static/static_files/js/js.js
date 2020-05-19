
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
    









    $('.gallery-image').click(function(){
        tab = $(".show_image_tab")
        src = $(this).attr('src');

        $('.image-big-src').attr('src', src);
        console.log(src);

        $(tab).css({
            display: 'block',
        });
        $(tab).animate({
            opacity:1,
        },200);
    });
    $('.close_image').click(function(){
        $(".show_image_tab").css({
            display: 'none',
            opacity:0,
        });
    });



});