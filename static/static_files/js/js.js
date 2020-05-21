
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

    // gallery
        var images_count = parseInt($('.images_count').text());
        var all = [];
        var all_numbers = [];
        var all_src = [];
        var active = false;
        var current_picture = '';


        function get_images(){
            for(var i = 1; i<=images_count; i++ ){
                all.push('image'+i.toString());
                all_src.push($('#image'+i.toString()).attr('src'));
                all_numbers.push(i)
            };
        };

        function show_image(){

            $('.image-big-src').attr('src', all_src[parseInt(current_picture.substring(5))-1]);
            $('.current_iamge').text(current_picture.substring(5));
            $('.max_images').text(all_numbers.length);
        };



        $('.gallery-image').click(function(){

            if(active === false){
                active = true;

                tab = $(".show_image_tab")
                src = $(this).attr('src');
                
                current_picture = this.id;

                get_images();
                show_image();



                $(tab).css({
                    display: 'block',
                });
                $(tab).animate({
                    opacity:1,
                },200);

        }
        });
        
        $('.arrow_next').click(function(){
            number = parseInt(current_picture.substring(5))+1;
            if( number <= all_numbers.length ){
                current_picture = 'iamge'+number.toString();
                show_image();
            }
        });
        
        $('.arrow_back').click(function(){
            number = parseInt(current_picture.substring(5))-1;
            if( number >= all_numbers[0] ){
                current_picture = 'iamge'+number.toString();
                show_image();
            }
        });



        $('.close_image').click(function(){
            all = [];
            all_src = [];
            all_numbers = [];
            active = false;
            $(".show_image_tab").css({
                display: 'none',
                opacity:0,
            });
        });



});


