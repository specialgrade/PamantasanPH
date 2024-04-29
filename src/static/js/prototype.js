// slideshow
const slides = document.querySelectorAll('.slides');
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
let currentSlide = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === index) {
      slide.classList.add('active');
    }
  });
}

prev.addEventListener('click', () => {
  currentSlide--;
  if (currentSlide < 0) {
    currentSlide = slides.length - 1;
  }
  showSlide(currentSlide);
});

next.addEventListener('click', () => {
  currentSlide++;
  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }
  showSlide(currentSlide);
});

showSlide(currentSlide);

// search bar & search button
const searchButton = document.getElementById("search-button");
searchButton.addEventListener("click", function() {
  const searchInput = document.getElementById("search-input");
  const searchTerm = searchInput.value.trim(); // Trim whitespace from the input
  if (searchTerm !== "") { // Check if the search term is not empty
    console.log(`Searching for: ${searchTerm}`);
  } else {
    console.log("Please enter a search term.");
  }
});
