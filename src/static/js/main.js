<<<<<<< HEAD
// Slideshow function
=======
// Slideshow  
>>>>>>> 32009e5584ac9f93a7bc2c4ad3181539d5d9ffc9
const slides = document.querySelectorAll('.slides');
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
let currentSlide = 0;

function showSlide(index) {
    slides.forEach((slide, i) => {
      if (i === index) {
        slide.style.display = "block"; 
      } else {
        slide.style.display = "none";
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



//Searchbar  
const items = [
  "City of Malabon University",
  "Dr. Filemon C. Aguilar Memorial College of Las Pinas",
  "Eulogio Amang Rodriguez Institute of Science & Technology",
  "Marikina Polytechnic College",
  "Navotas Polytechnic College",
  "Paranaque City College",
  "Polytechnic College of the City of Meycauayan",
  "Pamantasan ng Lungsod ng Maynila",
  "Pamantasan ng Lungsod ng Marikina",
  "Pamantasan ng Lungsod ng Muntinlupa",
  "Pamantasan ng Lungsod ng Pasig",
  "Pamantasan ng Valenzuela",
  "Philippine Normal University Manila",
  "Philippine State College of Aeronautics",
  "Polytechnic University of the Philippines",
  "Taguig City University",
  "Technological University of the Philippines",
  "Universidad de Manila",
  "Universidad de Makati",
  "University of the Philippines",
  "Quezon City University"
];

const itemToHtmlFileMap = {
  "City of Malabon University": "/home/universities/city-of-malabon-university",
  "Dr. Filemon C. Aguilar Memorial College of Las Pinas": "/home/universities/dr-filemon-c-aguilar-memorial-college-of-las-pinas",
  "Eulogio Amang Rodriguez Institute of Science & Technology": "/home/universities/eulogio-amang-rodriguez-institute-of-science-&-technology",
  "Marikina Polytechnic College": "/home/universities/marikina-polytechnic-college",
  "Navotas Polytechnic College": "/home/universities/navotas-polytechnic-college",
  "Paranaque City College":"/home/universities/paranaque-city-college",
  "Polytechnic College of the City of Meycauayan": "/home/universities/polytechnic-college-of-the-city-of Meycauayan",
  "Pamantasan ng Lungsod ng Maynila": "/home/universities/pamantasan-ng-lungsod-ng-maynila",
  "Pamantasan ng Lungsod ng Marikina": "/home/universities/pamantasan-ng-lungsod-ng-marikina",
  "Pamantasan ng Lungsod ng Muntinlupa": "/home/universities/pamantasan-ng-lungsod-ng-muntinlupa",
  "Pamantasan ng Lungsod ng Pasig": "/home/universities/pamantasan-ng-lungsod-ng-pasig",
  "Pamantasan ng Valenzuela": "/home/universities/pamantasan-ng-lungsod-ng-valenzuela",
  "Philippine Normal University Manila": "/home/universities/philippine-national-university" ,
  "Philippine State College of Aeronautics": "/home/universities/philippine-state-college-of-aeronautics",
  "Polytechnic University of the Philippines": "/home/universities/polytechnic-university-of-the-philippines",
  "Quezon City University": "/home/universities/quezon-city-university",
  "Taguig City University": "/home/universities/taguig-city-university",
  "Technological University of the Philippines": "/home/universities/technological-university-of-the-philippines",
  "Universidad de Manila": "/home/universities/universidad-de-manila",
  "Universidad de Makati": "/home/universities/university-of-makati",
  "University of the Philippines": "/home/universities/university-of-the-philippines",
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
    searchResultsElement.innerHTML = "<p class='no-results'>No results found</p>";
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

<<<<<<< HEAD
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
=======
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('newsletter-form').addEventListener('submit', function (event) {
      event.preventDefault(); 

      var email = document.getElementById('email').value;

      var emailPattern = /^[^\s@]+@gmail\.com$/;

        if (!emailPattern.test(email)) {
            alert("Please enter a valid email");
            return;
        }

      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/check_email', true);
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
              var response = JSON.parse(xhr.responseText);
              if (response.exists) {
                  alert("You've already subscribed!");
              } else {
                  alert("Subscribed successfully!");
                  document.getElementById('newsletter-form').submit(); 
              }
          }
      };
      xhr.send(JSON.stringify({ email: email }));
  });
});
>>>>>>> 32009e5584ac9f93a7bc2c4ad3181539d5d9ffc9
