const navBar = document.querySelector(".navBar");

window.addEventListener("scroll", handleScroll);

function handleScroll() {
  const isTop = window.scrollY === 0;
  navBar.classList.toggle("bg-gray-900", !isTop);
  navBar.classList.toggle("bg-transparent", isTop);
}

handleScroll();
