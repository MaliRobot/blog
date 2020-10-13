$(window).on('load', function() {
    var color = 0;
    $('.invisible_box').on('click', function(e) {
        let colors = [
            'aliceblue',
            'antiquewhite',
            'azure',
            'beige',
            'cornsilk',
            'ghostwhite',
            'honeydew',
            'papayawhip'
        ];
        if (color > colors.length - 1) {
            color = 0;
        }
        console.log(color);
        $(this).css('background-color', colors[color]);
        $('body').css('background-color', colors[color]);
        color++;
    });
});

$(document).ready(function (){
    function msieversion()
    {
        var ua = window.navigator.userAgent;
        var msie = ua.indexOf("MSIE ");

        if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./))  // If Internet Explorer, return version number
        {
            return true;
        }

        return false;
    }

    if (msieversion())
    {
        console.log('as');
        $('#menu-links').removeClass('col-md-2');
    }
})