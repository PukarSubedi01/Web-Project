$(window).on('scroll', function () { //function to make nav bar white on scroll
    if ($(window).scrollTop()) {
        $('nav').addClass('navCustom');
    } else {
        $('nav').removeClass('navCustom');

    }
})
$('.login').on('click', function () { //function to pop-up login form
    $('.LoginForm').css('display', 'flex');
});

$('.close').on('click', function () { //function to close login form
    $('.LoginForm').css('display', 'none');
});



$('.navbar-toggler').on('click', function () { //making nav bar white when clicked on toggle button.
    $('nav').addClass('navCustom')
});