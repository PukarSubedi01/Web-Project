//start of searching by ajax block
$(document).ready(function() {
    $("#searchInv").keyup(()=>{
        $.ajax({
            data:{searchInv:$("#searchInv").val()}, //searching invoices
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
            data:{searchItem:$("#searchItem").val()}, //searching item
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
            data:{searchCustomers:$("#searchCustomers").val()}, //searching customers
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
            data:{searchBills:$("#searchBills").val()}, //searching bills
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
            data:{searchVendors:$("#searchVendors").val()}, //seraching vendors
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
    //end of search block


    $(".sideMenuToggler").on("click", function (){ //this script activates class named activate onclick of dashboard toggle button
        $(".wrapper").toggleClass("activate");
    });

});

//calculating total amount in bills and invoives
function setTotal(){
    let quantity = document.getElementById('quantity').value;
    let price = document.getElementById('price').value;
    let tax = document.getElementById('tax').value;
    let total=parseInt(((tax/100)*price)+parseInt(price))*quantity;
    document.getElementById('total').value=total;

}
// submit data form validation block
function check_fields($event,errorMsgs){    //takes to argument of id's as a parameter where 1st one is textfield id and other error msg span id
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
           let selectVal = $("#selectVal").val();
            if (itemName=="" || quantity=="" || purchase_price=="" || sales_price=="" || tax=="" || date=="" || selectVal==null) {
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
//this disables pagination to decrease from 1
if($("#page").val() == 1){
    $("#prev").prop("disabled",true)
}

