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

//
function setTotal(){
    let quantity = document.getElementById('quantity').value;
    let price = document.getElementById('price').value;
    let tax = document.getElementById('tax').value;
    let total=parseInt(((tax/100)*price)+parseInt(price))*quantity;
    document.getElementById('total').value=total;

}