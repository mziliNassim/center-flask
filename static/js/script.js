const navBar = document.querySelector(".navBar");

window.addEventListener("scroll", handleScroll);

function handleScroll() {
  const isTop = window.scrollY === 0;
  navBar.classList.toggle("bg-gray-900", !isTop);
  navBar.classList.toggle("bg-transparent", isTop);
}

handleScroll();

// =============
let dropdownToggle = document.querySelector(".dropdownToggle");
let dropdownMenu = document.querySelector(".dropdownMenu");

function handleClick() {
  if (dropdownMenu.className.includes("block")) {
    dropdownMenu.classList.add("hidden");
    dropdownMenu.classList.remove("block");
  } else {
    dropdownMenu.classList.add("block");
    dropdownMenu.classList.remove("hidden");
  }
}

dropdownToggle?.addEventListener("click", handleClick);

// =============
const alert = document.querySelector(".alert");
const closeAlert = document.querySelector(".closeAlert");

setTimeout(() => {
  alert?.classList.add("hidden");
}, 2000);

closeAlert?.addEventListener("click", () => {
  alert.classList.add("hidden");
});

// =============
const inputPassword = document.querySelector(".input-password");
const eyePassword = document.querySelector(".eye-password");

eyePassword?.addEventListener("click", () => {
  if (inputPassword?.type === "password") {
    inputPassword.type = "text";
    eyePassword.classList.add("bi-eye-slash");
    eyePassword.classList.remove("bi-eye");
  } else {
    eyePassword.classList.remove("bi-eye-slash");
    eyePassword.classList.add("bi-eye");
    inputPassword.type = "password";
  }
});
