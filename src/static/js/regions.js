document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('.search input[type="text"]');
    const searchButton = document.querySelector('.search button');
    const resultBox = document.querySelector('.result-box');
  
    const schools = [
      'City of Malabon University',
      'Dr. Filemon C. Aguilar Memorial College of Las Piñas',
      'Eulogio "Amang" Rodriguez Institute of Science & Technology (EARIST)',
      'Marikina Polytechnic College',
      'Navotas Polytechnic College',
      'Pamantasan ng Lungsod ng Marikina',
      'Pamantasan ng Lungsod ng Maynila',
      'Pamantasan ng Lungsod ng Muntinlupa',
      'Pamantasan ng Lungsod ng Pasig',
      'Pamantasan ng Valenzuela',
      'Parañaque City College',
      'Philippine Normal University',
      'Philippine State College of Aeronautics',
      'Polytechnic College of the City of Meycauayan',
      'Polytechnic University of the Philippines',
      'Quezon City University',
      'Taguig City University',
      'Technological University of the Philippines',
      'Universidad de Manila',
      'University of Makati',
      'University of the Philippines',
      'Adiong Memorial State College',
      'Balabagan Trade School',
      'Basilan State College',
      'Cotabato Foundation College of Science and Technology',
      'Cotabato State University',
      'Hadji Butu School of Arts and Trades',
      'Lanao Agricultural College',
      'Lapak Agricultural School',
      'Mindanao State University',
      'Regional Madrasah Graduate Academy',
      'Sulu State College',
      'Tawi-tawi Regional Agricultural College',
      'Unda Memorial National Agricultural School',
      'University of Southern Mindanao',
      'Upi Agricultural School',
      'Abra State Institute of Science and Technology',
      'Apayao State College',
      'Benguet State University',
      'Ifugao State University',
      'Kalinga State University',
      'Mountain Province State University',
      'Philippine Military Academy',
      'Binalatongan Community College',
      'Don Mariano Marcos Memorial State University',
      'Ilocos Sur Polytechnic State College',
      'Mariano Marcos State University',
      'Pangasinan State University',
      'University of Northern Philippines',
      'Batanes State College',
      'Cagayan State University',
      'Isabela State University',
      'Nueva Vizcaya State University',
      'Quirino State University',
      'Bulacan Agricultural State College',
      'Bulacan State University',
      'Central Luzon State University',
      'Don Honorio Ventura State University',
      'Nueva Ecija University of Science and Technology',
      'Batangas State University',
      'Cavite State University',
      'Laguna State Polytechnic University',
      'Southern Luzon State University',
      'University of Rizal System',
      'Baco Community College',
      'City College of Calapan',
      'Marinduque State College',
      'Mindoro State University',
      'Occidental Mindoro State College',
      'Palawan State University',
      'Pola Community College',
      'Romblon State University',
      'Western Philippines University',
      'Bicol State College of Applied Sciences and Technology',
      'Bicol University',
      'Catanduanes State University',
      'Central Bicol State University of Agriculture',
      'Partido State University',
      'Bago City College',
      'Carlos Hilado Memorial State University',
      'La Carlota City College',
      'Philippine Normal University',
      'West Visayas State University',
      'Bohol Island State University',
      'Cebu Normal University',
      'Cebu Technological University',
      'Negros Oriental State University',
      'Siquijor State College',
      'Eastern Samar State University',
      'Eastern Visayas State University',
      'Leyte Normal University',
      'Palompon Institute of Technology',
      'University of Eastern Philippines',
      'Basilan State College',
      'JH Cerilles State College',
      'Jose Rizal Memorial State University',
      'Western Mindanao State University',
      'Zamboanga State College of Marine Sciences and Technology',
      'Bukidnon State University',
      'Central Mindanao University',
      'Camiguin Polytechnic State College',
      'Northwestern Mindanao State College of Science and Technology',
      'University of Science and Technology of Southern Philippines',
      'Davao del Norte State College',
      'Davao del Sur State College',
      'Davao Oriental State University',
      'Southern Philippines Agri-Business and Marine and Aquatic School of Technology',
      'University of Southern Philippines',
      'Cotabato Foundation College of Science and Technology',
      'South Cotabato State College',
      'Sultan Kudarat State University',
      'University of Southern Mindanao',
      'Agusan del Sur State College of Agriculture and Technology',
      'CARAGA State University',
      'Hinatuan Southern College',
      'North Eastern Mindanao State University',
      'Surigao del Norte State University',
      'University of Southeastern Philippines'
    ];
  
    searchButton.addEventListener('click', function () {
      const searchTerm = searchInput.value.trim().toLowerCase();
      
      // Filter schools based on search term
      const filteredSchools = schools.filter(school => school.toLowerCase().includes(searchTerm));
      
      if (searchTerm !== '' && filteredSchools.length > 0) {
        resultBox.style.display = 'block';
        // Display search results
        resultBox.innerHTML = filteredSchools.map(school => `<div class="result-item">${school}</div>`).join('');
      } else {
        resultBox.style.display = 'none';
        resultBox.innerHTML = ''; // Clear previous results
      }
    });
  
    // Hide result box when clicking outside of it
    document.addEventListener('click', function (event) {
      if (!searchButton.contains(event.target) && !resultBox.contains(event.target) && !searchInput.contains(event.target)) {
        resultBox.style.display = 'none';
      }
    });
  });