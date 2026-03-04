function togglePassword(){

    const password = document.getElementById("password");

    if(password.type === "password"){
        password.type = "text";
    } else {
        password.type = "password";
    }

}

const eyeBtn = document.getElementById("eyeBtn");
const password = document.getElementById("password");

eyeBtn.addEventListener("click", function () {

    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }

});