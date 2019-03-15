menuNav = document.querySelector('.menu-nav');
hamburgerBtn = document.querySelector('.hamburger-menu');

hamburgerBtn.onclick = () => {
    menuNav.classList.toggle('active');
}