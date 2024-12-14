const navBar = document.querySelector(".navBar");

window.addEventListener("scroll", handleScroll);

function handleScroll() {
  const isTop = window.scrollY === 0;
  navBar.classList.toggle("bg-gray-900", !isTop);
  navBar.classList.toggle("bg-transparent", isTop);
}

handleScroll();

// =============
const inputPassword = document.querySelector(".input-password");
const eyePassword = document.querySelector(".eye-password");

eyePassword.addEventListener("click", () => {
  if (inputPassword.type === "password") {
    inputPassword.type = "text";
    eyePassword.classList.add("bi-eye-slash");
    eyePassword.classList.remove("bi-eye");
  } else {
    eyePassword.classList.remove("bi-eye-slash");
    eyePassword.classList.add("bi-eye");
    inputPassword.type = "password";
  }
});
