//searching by ajax block
$(document).ready(function() {
    $("#searchInv").keyup(()=>{
        $.ajax({
            data:{searchInv:$("#searchInv").val()},
            url:'/searchInv',
            method:'GET',
            success:function(data){
                 $("tr").not("tr:first").remove();
                var html;
                for(d of data){
                    html="<tr>";
                    html+="<td>"+d.id+"</td>";
	                html+="<td>"+d.customer_id+"</td>";
                    html+="<td>"+d.items+"</td>";
                    html+="<td>"+d.total+"</td>";
                    html+="<td>"+d.invoice_date+"</td>";
                    html+="<td><a href='/edit/invoice/"+d.id+"'>edit</a>|<a href='/delete/invoice/"+d.id+"'>delete</a></td>"
                    html+="</tr>";
                     $("table").append(html);
                     }
        }, error:function(error){
        }, complete:function(){
        }
        });
     });
      $("#searchItem").keyup(()=>{
        $.ajax({
            data:{searchItem:$("#searchItem").val()},
            url:'/searchItem',
            method:'GET',
            success:function(data){
                 $("tr").not("tr:first").remove();
                var html;
                for(d of data){
                    html="<tr>";
                    html+="<td>"+d.item_name+"</td>";
	                html+="<td>"+d.quantity+"</td>";
                    html+="<td>"+d.sales_price+"</td>";
                    html+="<td>"+d.purchase_price+"</td>";
                    html+="<td>"+d.tax+"</td>";
                    html+="<td><a href='/edit/item/"+d.id+"'>edit</a>|<a href='/delete/item/"+d.id+"'>delete</a></td>"
                    html+="</tr>";
                     $("table").append(html);
                     }
        }, error:function(error){
        }, complete:function(){
        }
        });
     });

     $("#searchCustomers").keyup(()=>{
        $.ajax({
            data:{searchCustomers:$("#searchCustomers").val()},
            url:'/searchCustomers',
            method:'GET',
            success:function(data){
                 $("tr").not("tr:first").remove();
                var html;
                for(d of data){
                    html="<tr>";
                    html+="<td>"+d.name+"</td>";
	                html+="<td>"+d.email+"</td>";
                    html+="<td>"+d.phone+"</td>";
                    html+="<td>"+d.address+"</td>";
                    html+="<td><a href='/edit/customer/"+d.id+"'>edit</a>|<a href='/delete/customer/"+d.id+"'>delete</a></td>"
                    html+="</tr>";
                     $("table").append(html);
                     }
        }, error:function(error){
        }, complete:function(){
        }
        });
     });

      $("#searchBills").keyup(()=>{
        $.ajax({
            data:{searchBills:$("#searchBills").val()},
            url:'/searchBills',
            method:'GET',
            success:function(data){
                 $("tr").not("tr:first").remove();
                var html;
                for(d of data){
                    html="<tr>";
                    html+="<td>"+d.id+"</td>";
	                html+="<td>"+d.vendor_id+"</td>";
                    html+="<td>"+d.items+"</td>";
                    html+="<td>"+d.total+"</td>";
                    html+="<td>"+d.bill_date+"</td>";
                    html+="<td><a href='/edit/bill/"+d.id+"'>edit</a>|<a href='/delete/bill/"+d.id+"'>delete</a></td>"
                    html+="</tr>";
                     $("table").append(html);
                     }
        }, error:function(error){
        }, complete:function(){
        }
        });
     });

     $("#searchVendors").keyup(()=>{
        $.ajax({
            data:{searchVendors:$("#searchVendors").val()},
            url:'/searchVendors',
            method:'GET',
            success:function(data){
                 $("tr").not("tr:first").remove();
                var html;
              for(d of data){
                    html="<tr>";
                    html+="<td>"+d.name+"</td>";
	                html+="<td>"+d.email+"</td>";
                    html+="<td>"+d.phone+"</td>";
                    html+="<td>"+d.address+"</td>";
                    html+="<td><a href='/edit/vendor/"+d.id+"'>edit</a>|<a href='/delete/vendor/"+d.id+"'>delete</a></td>"
                    html+="</tr>";
                     $("table").append(html);
                     }
        }, error:function(error){
        }, complete:function(){
        }
        });
     });

    $(".sideMenuToggler").on("click", function (){
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


//form validation block
//$(document).ready(function() {
//
//         $("#error_messageName").hide();
//          $("#error_messagQnty").hide();
//          $("#error_messagePurchase").hide();
//          $("#error_messageSales").hide();
//          $("#error_messageTax").hide();
//
//         var error_name = false;
//         var error_email = false;
//         var error_password = false;
//         var error_retype_password = false;
//         $(".fields").focusout(function(){
//            check_fields();
//         });
//
//
//
//         function check_fields() {
//            var fieldValue = $(".fields").val();
//            if (fieldValue !== '') {
//               $(".error_message").hide();
//               $(".fields").css("border","2px solid #34F458");
//            } else {
//               $(".error_message").html("*required");
//               $(".error_message").show();
//               $(".fields").css("border","2px solid #F90A0A");
//               error_name = true;
//            }
//         }
//
//
//
//         function check_email() {
//            var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
//            var email = $("#email").val();
//            if (pattern.test(email) && email !== '') {
//               $("#email_error_message").hide();
//               $("#email").css("border","2px solid #34F458");
//            } else {
//               $("#email_error_message").html("*Invalid Email");
//               $("#email_error_message").show();
//               $("#email").css("border","2px solid #F90A0A");
//               error_email = true;
//            }
//         }
//         $("#newInvForm").submit(function() {
//            error_fullname = false;
//            error_email = false;
//            error_password = false;
//            error_retype_password = false;
//
//            check_fullName();
//            check_email();
//            check_password();
//            check_retype_password();
//
//            if (error_fullname === false && error_email === false && error_password === false && error_retype_password === false) {
//               alert("Registration Successfull");
//               return true;
//            } else {
//               alert("Please correctly fill all the fields");
//               return false;
//            }
//
//         });
//      });

//calculating total amount in bills and invoives
function setTotal(){
    let quantity = document.getElementById('quantity').value;
    let price = document.getElementById('price').value;
    let tax = document.getElementById('tax').value;
    let total=parseInt(((tax/100)*price)+parseInt(price))*quantity;
    document.getElementById('total').value=total;

}

function check_fields($event,errorMsgs){
     var fieldValue = $("#"+$event.getAttribute("id")).val();
            if (fieldValue !== '') {
               $("#"+errorMsgs).hide();

            } else {
               $("#"+errorMsgs).html("*required");
               $("#"+errorMsgs).css("color","red")
               $("#"+errorMsgs).css("margin-left","2%")
               $("#"+errorMsgs).show();
               errorMsgs = true;
            }
    }
    $("#NewItemForm").submit(function() {
           let itemName = $("#itemName").val();
           let quantity = $("#qnty").val();
           let purchase_price = $("#pPrice").val();
           let sales_price = $("#sPrice").val();
           let tax = $("#tax").val();


            if (itemName=="" || quantity=="" || purchase_price=="" || sales_price=="" || tax=="") {
               alert("Please correctly fill all the fields");
               return false;
            } else {
               alert("Saved successfully");
               return true;
            }

         });
         $("#new").submit(function() {
           let itemName = $("#itemName").val();
           let date = $("#Date").val();
           let quantity = $("#quantity").val();
           let purchase_price = $("#price").val();
           let sales_price = $("#tax").val();
           let tax = $("#total").val();


            if (itemName=="" || quantity=="" || purchase_price=="" || sales_price=="" || tax=="" || date=="") {
               alert("Please correctly fill all the fields");
               return false;
            } else {
               alert("Saved successfully");
               return true;
            }

         });
          $("#custVend").submit(function() {
           let name = $("#name").val();
           let email = $("#email").val();
           let phone = $("#phn").val();
           let address = $("#address").val();



            if (name=="" || email=="" || phone=="" || address=="") {
               alert("Please correctly fill all the fields");
               return false;
            } else {
               alert("Saved successfully");
               return true;
            }

         });

if($("#page").val() == 1){
    $("#prev").prop("disabled",true)
}