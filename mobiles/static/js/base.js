
//side nav config
function openNav() {
    document.getElementById("mySidenav").style.width = "100vw";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


//login signup popup scripts
function openloginForm() {
    visibility = document.querySelector("#form-visible");
    visibility.className += " visible";
    document.querySelector("#login-form").style.display = "block"
    document.querySelector("#signup-form").style.display = "none"
}

function closeloginForm() {
    visibility = document.querySelector("#form-visible");
    visibility.className = "form-group";
    document.querySelector("#login-form").style.display = "none"
}

function opensignupForm() {
    visibility = document.querySelector("#form-visible");
    visibility.className += " visible";
    document.querySelector("#signup-form").style.display = "block"
    document.querySelector("#login-form").style.display = "none"
}

function closesignupForm() {
    visibility = document.querySelector("#form-visible");
    visibility.className = "form-group";
    document.querySelector("#signup-form").style.display = "none"
}