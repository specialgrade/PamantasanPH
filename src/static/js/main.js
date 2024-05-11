// Slideshow function
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


//Searchbar function
const items = [
  "Polytechnic University of the Philippines",
  "Taguig City University",
  "Technological University of the Philippines",
  "Universidad de Manila",
  "Universidad de Makati",
  "University of the Philippines",
  "Quezon City University"
];

const itemToHtmlFileMap = {
  "Polytechnic University of the Philippines": "src/templates/univs/pup.html",
  "Taguig City University": "Taguig City University.html",
  "Technological University of the Philippines": "Technological University of the Philippines.html",
  "Universidad de Manila": "Universidad de Manila.html",
  "Universidad de Makati": "Universidad de Makati.html",
  "University of the Philippines": "University of the Philippines.html",
  "Quezon City University": "Quezon City University.html"
};

document.addEventListener("DOMContentLoaded", function() {
  const searchInput = document.getElementById("search-input");
  const searchButton = document.getElementById("search-button");

  searchInput.addEventListener("input", filterItems);
  searchButton.addEventListener("click", filterItems);
});

function filterItems() {
  const searchTerm = document.getElementById("search-input").value.toLowerCase();
  const filteredItems = items.filter(item => item.toLowerCase().includes(searchTerm));
  
  if (searchTerm) {
    displayResults(filteredItems);
  } else {
    hideResults();
  }
}

function displayResults(results) {
  const searchResultsElement = document.getElementById("searchResults");
  searchResultsElement.style.display = "block";
  searchResultsElement.innerHTML = "";

  if (results.length === 0) {
    searchResultsElement.innerHTML = "<p>No results found</p>";
  } else {
    results.forEach(result => {
      const resultItem = document.createElement("div");
      const link = document.createElement("a");
      const span = document.createElement("span");
      
      const htmlFile = itemToHtmlFileMap[result];
      
      link.href = htmlFile + `#${result.replace(/\s+/g, "_")}`;
      link.style.textDecoration = "none";
      span.textContent = result;
      span.style.color = "black";
      link.appendChild(span);
      resultItem.appendChild(link);
      
      resultItem.classList.add("result-item");
      searchResultsElement.appendChild(resultItem);
      searchResultsElement.appendChild(document.createElement("br")); 
    });
  }
}

function hideResults() {
  const searchResultsElement = document.getElementById("searchResults");
  searchResultsElement.style.display = "none";
}