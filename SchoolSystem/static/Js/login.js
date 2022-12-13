window.onload = function() {
    setTimeout(function() {
        var Spinner = document.getElementById('preloader');
        Spinner.style.display = 'none';
        var Spinner = document.getElementById('form');
        Spinner.style.display = 'flex';
    }, 1000)

}

setTimeout(function() {
    let message = document.getElementById('message');
    message.style.display = "none";
}, 15000)

var btn = document.getElementById('login_btn');
var login_spinner = document.getElementById('login_spinner');


