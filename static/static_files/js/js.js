$(document).ready(function(){
    var console = $('.console');
    var start = $('.start');
    var start_position = start.position();
    var content = $('#content');
    console.text('start : y: '+start_position.top+' x: '+start_position.left);
    
    window.addEventListener('resize', function(event){
        start_position = start.position();
        console.text('start : y: '+start_position.top+' x: '+start_position.left);


      });






});