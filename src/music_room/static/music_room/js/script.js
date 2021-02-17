$(function () {

    $('.navbar-toggler').on('click', function() {
        if (!$('#mainNav').hasClass('navbar-reduce')) {
          $('#mainNav').addClass('navbar-reduce');
        }
    });

    // Back to top button
    $('.back-to-top').on('click', function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1000, 'easeInOutExpo');
        return false;
    });

    // navbar-toggler button
    $('.toggle-button').on('click', function () {
        $('.animated-icon').toggleClass('open');
    });

    /*--/ Navbar Menu Reduce /--*/
    $(window).trigger("scroll");
    $(window).on("scroll", function() {
        const pixels = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
        if ($(window).scrollTop() > pixels) {
            $(".navbar-expand-md").addClass("bg-light");
            $(".navbar-expand-md").addClass("shadow");
            $(".navbar-expand-md").addClass("navbar-reduce");
            $(".navbar-expand-md").removeClass("navbar-trans");
            $('.dropdown-menu').removeClass('dropdown-trans');
            $('.dropdown-menu').addClass('dropdown-reduce');
            $('.back-to-top').fadeIn('slow');
        } else {
            if (!$("#navbarDefault").hasClass("show")) {
                $(".navbar-expand-md").removeClass("bg-light");
                $(".navbar-expand-md").removeClass("shadow");
                $(".navbar-expand-md").removeClass("navbar-reduce");
                $('.dropdown-menu').removeClass('dropdown-reduce');
            }
            $(".navbar-expand-md").addClass("navbar-trans");
            $('.dropdown-menu').addClass('dropdown-trans');
            $('.back-to-top').fadeOut('slow');
        }
    });
});(jQuery);
