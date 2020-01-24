$(document).ready(function () {
    $(".sideMenuToggler").on("click", function () {
        $(".wrapper").toggleClass("active");
    });
    $(".tree1").on("click", function () {
        $(".nested1").toggleClass("nesting1");
        // $(".nested2").toggleClass("nesting");
    });
    $(".tree2").on("click", function () {
        $(".nested2").toggleClass("nesting2");
        // $(".nested2").toggleClass("nesting");
    });
});