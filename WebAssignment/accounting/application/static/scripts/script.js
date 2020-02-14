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

$(document).ready(function() {

         $("#name_error_message").hide();
         $("#email_error_message").hide();
         $("#password_error_message").hide();
         $("#rePsw_password_error_message").hide();

         var error_name = false;
         var error_email = false;
         var error_password = false;
         var error_retype_password = false;
         $("#fullname").focusout(function(){
            check_fullName();
         });

         $("#email").focusout(function() {
            check_email();
         });
         $("#password").focusout(function() {
            check_password();
         });
         $("#re-password").focusout(function() {
            check_retype_password();
         });

         function check_fullName() {
            var pattern = /^[a-zA-Z\-\s]+$/;
            var name = $("#fullname").val();
            if (pattern.test(name) && name !== '') {
               $("#name_error_message").hide();
               $("#fullname").css("border","2px solid #34F458");
            } else {
               $("#name_error_message").html("*Should contain only Characters");
               $("#name_error_message").show();
               $("#fullname").css("border","2px solid #F90A0A");
               error_name = true;
            }
         }

         function check_password() {
            var password_length = $("#password").val().length;
            if (password_length < 8) {
               $("#password_error_message").html("*Atleast 8 Characters");
               $("#password_error_message").show();
               $("#password").css("border","2px solid #F90A0A");
               error_password = true;
            } else {
               $("#password_error_message").hide();
               $("#password").css("border","2px solid #34F458");
            }
         }

         function check_retype_password() {
            var password = $("#password").val();
            var retype_password = $("#re-password").val();
            if (password !== retype_password) {
               $("#rePsw_error_message").html("*Passwords Did not Matched");
               $("#rePsw_error_message").show();
               $("#re-password").css("border","2px solid #F90A0A");
               error_retype_password = true;
            } else {
               $("#rePsw_error_message").hide();
               $("#re-password").css("border","2px solid #34F458");
            }
         }

         function check_email() {
            var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
            var email = $("#email").val();
            if (pattern.test(email) && email !== '') {
               $("#email_error_message").hide();
               $("#email").css("border","2px solid #34F458");
            } else {
               $("#email_error_message").html("*Invalid Email");
               $("#email_error_message").show();
               $("#email").css("border","2px solid #F90A0A");
               error_email = true;
            }
         }
         $("#registration_form").submit(function() {
            error_fullname = false;
            error_email = false;
            error_password = false;
            error_retype_password = false;

            check_fullName();
            check_email();
            check_password();
            check_retype_password();

            if (error_fullname === false && error_email === false && error_password === false && error_retype_password === false) {
              
               return true;
            } else {
               alert("Please correctly fill all the fields");
               return false;
            }

         });
      });