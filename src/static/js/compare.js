const items = [
    "Polytechnic University of the Philippines",
    "Taguig City University",
    "Technological University of the Philippines",
    "Universidad de Manila",
    "Universidad de Makati",
    "University of the Philippines",
    "Quezon City University"
];

const itemToHtmlContentMap = {
    "Polytechnic University of the Philippines": "<h1>Polytechnic University of the Philippines</h1><p>Content for PUP</p>",
    "Taguig City University": "<h1>Taguig City University</h1><p>Content for TCU</p>",
    "Technological University of the Philippines": "<h1>Technological University of the Philippines</h1><p>Content for TUP</p>",
    "Universidad de Manila": "<h1>Universidad de Manila</h1><p>Content for UDM</p>",
    "Universidad de Makati": "<h1>Universidad de Makati</h1><p>Content for UMak</p>",
    "University of the Philippines": "<h1>University of the Philippines</h1><p>Content for UP</p>",
    "Quezon City University": "<h1>Quezon City University</h1><p>Content for QCU</p>"
};

function toggleDropdown(id) {
    document.getElementById(id).classList.toggle("show");
}

function selectUniversity(element, number) {
    const universityName = element.textContent;
    document.getElementById('university' + number).value = universityName;
    document.getElementById('dropdown' + number).classList.remove("show");
    loadUniversityContent(universityName, number);
}

function loadUniversityContent(universityName, number) {
    console.log(`Loading content for ${universityName} into university${number}Content`);
    const content = itemToHtmlContentMap[universityName];
    
    if (content) {
        console.log(`Successfully loaded content for ${universityName}`);
        document.getElementById('university' + number + 'Content').innerHTML = content;
    } else {
        console.error(`Failed to load content for ${universityName}: Content not found`);
        document.getElementById('university' + number + 'Content').innerHTML = '<p>Content not found</p>';
    }
}

function filterItems() {
    console.log("filterItems called");
    const searchTerm = document.getElementById("university1").value.toLowerCase();
    console.log("searchTerm:", searchTerm);
    const filteredItems = items.filter(item => item.toLowerCase().includes(searchTerm));
    console.log("filteredItems:", filteredItems);

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

            link.href = "#";
            link.onclick = function() {
                selectUniversity({ textContent: result }, 1);
                return false;
            };
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

document.getElementById("university1").addEventListener("input", filterItems);

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropdown-icon')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}