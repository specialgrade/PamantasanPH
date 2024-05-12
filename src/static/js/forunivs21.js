// Navbar
document.querySelector('.dropdown').addEventListener('click', function() {
  document.querySelector('.navbar').classList.toggle('responsive');
});

// Dropdown header
document.querySelectorAll('.dropdown-header').forEach(header => {
  header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      content.classList.toggle('active');
  });
});
