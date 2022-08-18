/* Project: Gillian Moore B&B Galway - Author: Jose Maria Rico Leal, StudentID:10539218
 Module:B8IT144 Web Design and Development */
var form = document.getElementById("contact-form");


$(document).ready(function() {
	$("#contact-form").submit(function(event) {

		var is_error = false;
		var error_count = 0;
	

		var first_name = $("#first_name").val();
		if (first_name == "") {
			$("input#first_name").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
			
			
		}

		var last_name = $("#last_name").val();
		if (last_name == "") {
			$("input#last_name").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
			
		}

		var address_first_line = $("#address_first_line").val();
		if (address_first_line == "") {
			$("input#address_first_line").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
		
		}

		var city = $("#city").val();
		if (city == "") {
			$("input#city").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
		
		}

		var email = $("#email").val();
		if (email == "") {
			$("input#email").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
		
		}
		var select = $("#select").val();
		if (email == "") {
			$("select#select").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
		
		}
		var check_in = $("#check_in").val();
		if (email == "") {
			$("input#check_in").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
		
		}
		var check_out = $("#check_out").val();
		if (email == "") {
			$("input#check_out").css("border-color", "#ff3333");
			is_error = true;
			error_count += 1;
		
		}

		

		if (is_error == true) {
			$("span#error-count").text(error_count);
			$("p#error-list").css("display", "block");
			event.preventDefault();			
		}

		
		$("#first_name").focusout(function(){
			$("input#first_name").css("border-color", "#dddddd");
		});
		$("#last_name").focusout(function(){
			$("input#last_name").css("border-color", "#dddddd");
		});
		$("#address_first_line").focusout(function(){
			$("input#address_first_line").css("border-color", "#dddddd");
		});
		$("#city").focusout(function(){
			$("input#city").css("border-color", "#dddddd");
		});
		$("#email").focusout(function(){
			$("input#email").css("border-color", "#dddddd");
		});
		$("#select").focusout(function(){
			$("select#select").css("border-color", "#dddddd");
		});
		$("#check_in").focusout(function(){
			$("input#check_in").css("border-color", "#dddddd");
		});
		$("#check_out").focusout(function(){
			$("input#check_out").css("border-color", "#dddddd");
		});
		
	});
});

 function print_out_error() {
            let inputFields = document.getElementsByClassName('form_input');
            let message =''; 
            for (var i = 0; i < inputFields.length; i++) {
                console.log(inputFields[i].value);
                if (inputFields[i].value === '') {
                        message = message + inputFields[i].getAttribute('name') + ', ';
                }
            }

            let n = message.lastIndexOf(",");
            message = message.substring(0,n); 

            document.querySelector('#fail-message').innerHTML =
                'Please fill out ' +
                message +
                ' field(s)';
        }




