menuNav = document.querySelector('.menu-nav');
hamburgerBtn = document.querySelector('.hamburger-menu');
toggleDropdown = document.querySelector('.toggle-dropdown');
dropdownMenu = document.querySelector('.dropdown-menu');
hamburgerArrows = document.querySelectorAll('.arrow');

hamburgerBtn.onclick = () => {
    menuNav.classList.toggle('active');
}

toggleDropdown.onclick = () => {
    dropdownMenu.classList.toggle('active');
}