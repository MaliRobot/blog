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