var resizeScreen = function() {
    // Navigation bar top padding
    var $navbar = $('#navbar');
    console.log($navbar.css('padding-top'));

    var navHeight = $navbar.outerHeight();
    $('.fixed-top-offset').height(navHeight);

    // Adjust iframe size
    var windowHeight = $(window).height();
    $('.full-height').height(windowHeight - navHeight - 5);
}

window.addEventListener('resize', resizeScreen);

var applyFeather = function() {
    try {
        feather.replace();
    } catch (err) {}
}