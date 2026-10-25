const loginTab=document.getElementById("loginTab");
const registerTab=document.getElementById("registerTab");

const loginForm=document.getElementById("loginForm");
const registerForm=document.getElementById("registerForm");

loginTab.addEventListener("click",()=>{

loginForm.classList.remove("hidden");
registerForm.classList.add("hidden");

loginTab.classList.add("active");
registerTab.classList.remove("active");

});

registerTab.addEventListener("click",()=>{

registerForm.classList.remove("hidden");
loginForm.classList.add("hidden");

registerTab.classList.add("active");
loginTab.classList.remove("active");

});

function togglePassword(id){

let field=document.getElementById(id);

if(field.type==="password")
field.type="text";
else
field.type="password";

}  

const glow = document.querySelector(".cursor-glow");

document.addEventListener("mousemove", (e) => {
    glow.style.left = e.clientX + "px";
    glow.style.top = e.clientY + "px";
});