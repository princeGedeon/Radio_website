"use strict";
// Show password js
let passwordInput = document.querySelector(".password-wrap input");
let showPassword = document.querySelector("#showPassword");
showPassword.addEventListener("click",()=>{ 
    showPassword.classList.toggle("active");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
});