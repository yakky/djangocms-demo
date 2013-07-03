$(document).ready(function() {
    if(document.location.hash == '#validated') {
        alert("Thank you\nYour email has been validated!");
    }
    if(document.location.hash == '#error') {
        alert("Sorry, an error occurred while\nvalidating your email address");
    }
    $(document).on("click", ".contact-open", function(event){
        event.preventDefault();
        $(".message").slideToggle();
        $(".contact").slideToggle();
    });
    $(document).on("click", ".contact-send", function(event){
        event.preventDefault();
        $button = $(this);
        data = $("input[type=email]", $button.parent()).val();
        if(data && validateEmail(data)) {
            $.post(post_url, {email:data}, function(data, text, XHR){
                alert("Thank you!\nWe will get to you soon!");
                $(".contact").slideToggle();
            })
        }
        else {
            alert("Please, provide a valid email address");
        }
    });
});