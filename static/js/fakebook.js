$(document).ready(function () {
    $("#signUpform").submit(function () {
        $.post('/addUser/', $(this).serialize(), function (response) {
            /* do something with returned data from server*/
            console.log(response);
            window.location.href = "/signIn/";
        });
        return false;
        /* prevent browser submitting form*/
    });
});


$(document).ready(function () {
    $("#signInform").submit(function () {
        $.post('/signIn/', $(this).serialize(), function (response) {
            /* do something with returned data from server*/
            console.log(response);

            if (response.success == true) {
                window.location.href = "/";
            } else {
                alert(response.error);
            }
        });
        return false;
        /* prevent browser submitting form*/
    });
});

$(document).ready(function () {
    $(".commentPost").submit(function () {
        $.post('/comment/', $(this).serialize(), function (response) {
            /* do something with returned data from server*/
            console.log(response);
            window.location.href = "/"
        });
        return false;
        /* prevent browser submitting form*/
    });
});

$(document).ready(function () {
    $("#userPost").submit(function () {
        $.post('/post/', $(this).serialize(), function (response) {
            /* do something with returned data from server*/
            console.log(response);
            window.location.href = "/"
        });
        return false;
        /* prevent browser submitting form*/
    });
});


$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");
	});

$(document).ajaxStart(function(){
    $('.se-pre-con').show();
 }).ajaxStop(function(){
    $('.se-pre-con').hide();
 });
