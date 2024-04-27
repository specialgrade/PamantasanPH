// let slideIndex = 1;
// showSlides(slideIndex);
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("slides");
//   let dots = document.getElementsByClassName("demo");
//   let captionText = document.getElementById("caption");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace("active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += "active";
//   captionText.innerHTML = dots[slideIndex-1].alt;
// }

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

showSlide(currentSlide);\

// search bar & search button
const searchButton = document.getElementById("search-button");
searchButton.addEventListener("click", function() {
  const searchInput = document.getElementById("search-input");
  const searchTerm = searchInput.value;
  console.log(`Searching for: ${searchTerm}`);
});