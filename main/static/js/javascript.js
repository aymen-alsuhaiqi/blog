document.getElementById("btn_nav").addEventListener("click", function (e) {
  if (!this.classList.contains("btn-right")) {
    this.classList.add("btn-right");
    this.textContent = "keyboard_double_arrow_right";
    document.getElementById("nav").classList.remove("nav");
    document.getElementById("nav").classList.add("side");
    const listItems = document.getElementsByTagName("li");
    for (let i = 0; i < listItems.length; i++) {
        listItems[i].classList.remove('visible');
        listItems[i].classList.add('hidden');
    }
} else {
    this.classList.remove("btn-right");
    this.textContent = "keyboard_double_arrow_left";
    document.getElementById("nav").classList.remove("side");
    document.getElementById("nav").classList.add("nav");
    const listItems = document.getElementsByTagName("li");
    setTimeout(() => {
        for (let i = 0; i < listItems.length; i++) {
            listItems[i].classList.remove('hidden');
            listItems[i].classList.add('visible');
        }
    },150)
  }
});
document.addEventListener("DOMContentLoaded", function () {
  const icon = document.querySelector(".btn-sidebar");
  const sidebar = document.querySelector(".side");

  icon.addEventListener("mouseover", function () {
    sidebar.style.borderRight = "3px blue solid";
  });

  icon.addEventListener("mouseout", function () {
    sidebar.style.borderRight = "3px rgb(92, 30, 30) solid";
  });
});
