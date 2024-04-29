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

// filter
let availableKeywords = [
    'ang pogi',
    'mo naman',
    'tadz sobra',
    'haysss',
  ];
  
  const resultsBox = document.querySelector(".result-box");
  const inputBox = document.getElementById("input-box");
  
  inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    if(input.length){
        result=availableKeywords.filter((keyword)=>{
        return keyword.toLowerCase().includes(input.toLocaleLowerCase());
        });
        console.log(result);
    }
    display(result);
    if(!result.length){
        resultsBox.innerHTML='';
    }
  }
  function display(result){
    resultsBox.innerHTML = ''; // Clear the previous content
    result.forEach((item) => {
        const listItem = document.createElement('li');
        listItem.textContent = item;
        listItem.addEventListener('click', () => selectInput(listItem));
        resultsBox.appendChild(listItem);
    });
  }
  
  
  function selectInput(list){
    inputBox.value = list.innerHTML;
    resultsBox.innerHTML='';
  }
