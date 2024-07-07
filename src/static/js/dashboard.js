document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.querySelector('.search input[type="text"]');
  const searchButton = document.querySelector('.search button');
  const resultBox = document.querySelector('.result-box');

  const schools = [
    { name: 'City of Malabon University', url: "{{ url_for('static', filename='templates/cmu.html') }}" },
    { name: 'Dr. Filemon C. Aguilar Memorial College of Las Piñas', url: "{{ url_for('static', filename='templates/dfcamclp.html') }}" },
    { name: 'Eulogio "Amang" Rodriguez Institute of Science & Technology (EARIST)', url: "{{ url_for('static', filename='templates/earist.html') }}" },
    { name: 'Marikina Polytechnic College', url: "{{ url_for('static', filename='templates/mpc.html') }}" },
    { name: 'Navotas Polytechnic College', url: "{{ url_for('static', filename='templates/npc.html') }}" },
    { name: 'Pamantasan ng Lungsod ng Marikina', url: "{{ url_for('static', filename='templates/plmar.html') }}" },
    { name: 'Pamantasan ng Lungsod ng Maynila', url: "{{ url_for('static', filename='templates/plm.html') }}" },
    { name: 'Pamantasan ng Lungsod ng Muntinlupa', url: "{{ url_for('static', filename='templates/plmun.html') }}" },
    { name: 'Pamantasan ng Lungsod ng Pasig', url: "{{ url_for('static', filename='templates/plpasig.html') }}" },
    { name: 'Pamantasan ng Valenzuela', url: "{{ url_for('static', filename='templates/pnv.html') }}" },
    { name: 'Parañaque City College', url: "{{ url_for('static', filename='templates/pcc.html') }}" },
    { name: 'Philippine Normal University', url: "{{ url_for('static', filename='templates/pnu.html') }}" },
    { name: 'Philippine State College of Aeronautics', url: "{{ url_for('static', filename='templates/psca.html') }}" },
    { name: 'Polytechnic College of the City of Meycauayan', url: "{{ url_for('static', filename='templates/pccm.html') }}" },
    { name: 'Polytechnic University of the Philippines', url: "{{ url_for('static', filename='templates/pup.html') }}" },
    { name: 'Quezon City University', url: "{{ url_for('static', filename='templates/qcu.html') }}" },
    { name: 'Taguig City University', url: "{{ url_for('static', filename='templates/tcu.html') }}" },
    { name: 'Technological University of the Philippines', url: "{{ url_for('static', filename='templates/tup.html') }}" },
    { name: 'Universidad de Manila', url: "{{ url_for('static', filename='templates/udm.html') }}" },
    { name: 'University of Makati', url: "{{ url_for('static', filename='templates/umak.html') }}" },
    { name: 'University of the Philippines', url: "{{ url_for('static', filename='templates/up.html') }}" },
    { name: 'Adiong Memorial State College', url: "{{ url_for('static', filename='templates/amsc.html') }}" },
    { name: 'Balabagan Trade School', url: "{{ url_for('static', filename='templates/bts.html') }}" },
    { name: 'Basilan State College', url: "{{ url_for('static', filename='templates/bsc.html') }}" },
    { name: 'Cotabato Foundation College of Science and Technology', url: "{{ url_for('static', filename='templates/cfcst.html') }}" },
    { name: 'Cotabato State University', url: "{{ url_for('static', filename='templates/csu.html') }}" },
    { name: 'Hadji Butu School of Arts and Trades', url: "{{ url_for('static', filename='templates/hbsat.html') }}" },
    { name: 'Lanao Agricultural College', url: "{{ url_for('static', filename='templates/lac.html') }}" },
    { name: 'Lapak Agricultural School', url: "{{ url_for('static', filename='templates/las.html') }}" },
    { name: 'Mindanao State University', url: "{{ url_for('static', filename='templates/msu.html') }}" },
    { name: 'Regional Madrasah Graduate Academy', url: "{{ url_for('static', filename='templates/rmga.html') }}" },
    { name: 'Sulu State College', url: "{{ url_for('static', filename='templates/ssc.html') }}" },
    { name: 'Tawi-tawi Regional Agricultural College', url: "{{ url_for('static', filename='templates/trac.html') }}" },
    { name: 'Unda Memorial National Agricultural School', url: "{{ url_for('static', filename='templates/umnas.html') }}" },
    { name: 'University of Southern Mindanao', url: "{{ url_for('static', filename='templates/universities/usm.html') }}" },
    { name: 'Upi Agricultural School', url: "{{ url_for('static', filename='templates/universities/uas.html') }}" },
    { name: 'Abra State Institute of Science and Technology', url: "{{ url_for('static', filename='templates/universities/asisat.html') }}" },
    { name: 'Apayao State College', url: "{{ url_for('static', filename='templates/universities/asc.html') }}" },
    { name: 'Benguet State University', url: "{{ url_for('static', filename='templates/universities/bsu.html') }}" },
    { name: 'Ifugao State University', url: "{{ url_for('static', filename='templates/universities/ifugao.html') }}" },
    { name: 'Kalinga State University', url: "{{ url_for('static', filename='templates/universities/ksu.html') }}" },
    { name: 'Mountain Province State University', url: "{{ url_for('static', filename='templates/universities/mpsu.html') }}" },
    { name: 'Philippine Military Academy', url: "{{ url_for('static', filename='templates/universities/pma.html') }}" },
    { name: 'Binalatongan Community College', url: "{{ url_for('static', filename='templates/universities/bcc.html') }}" },
    { name: 'Don Mariano Marcos Memorial State University', url: "{{ url_for('static', filename='templates/universities/dmmm.html') }}" },
    { name: 'Ilocos Sur Polytechnic State College', url: "{{ url_for('static', filename='templates/universities/iscps.html') }}" },
    { name: 'Mariano Marcos State University', url: "{{ url_for('static', filename='templates/universities/mmsu.html') }}" },
    { name: 'Pangasinan State University', url: "{{ url_for('static', filename='templates/universities/psu.html') }}" },
    { name: 'University of Northern Philippines', url: "{{ url_for('static', filename='templates/universities/unp.html') }}" },
    { name: 'Batanes State College', url: "{{ url_for('static', filename='templates/universities/bsc.html') }}" },
    { name: 'Cagayan State University', url: "{{ url_for('static', filename='templates/universities/csu.html') }}" },
    { name: 'Isabela State University', url: "{{ url_for('static', filename='templates/universities/isu.html') }}" },
    { name: 'Nueva Vizcaya State University', url: "{{ url_for('static', filename='templates/universities/nvsu.html') }}" },
    { name: 'Quirino State University', url: "{{ url_for('static', filename='templates/universities/qsu.html') }}" },
    { name: 'Bulacan Agricultural State College', url: "{{ url_for('static', filename='templates/universities/basc.html') }}" },
    { name: 'Bulacan Polytechnic College', url: "{{ url_for('static', filename='templates/universities/bpc.html') }}" },
    { name: 'Bulacan State University', url: "{{ url_for('static', filename='templates/universities/bsu.html') }}" },
    { name: 'Bustos Academy', url: "{{ url_for('static', filename='templates/universities/ba.html') }}" },
    { name: 'Central Luzon State University', url: "{{ url_for('static', filename='templates/universities/clsu.html') }}" },
    { name: 'Central Luzon Teachers College', url: "{{ url_for('static', filename='templates/universities/cltc.html') }}" },
    { name: 'Don Honorio Ventura State University', url: "{{ url_for('static', filename='templates/universities/dhvsu.html') }}" },
    { name: 'Gordon College', url: "{{ url_for('static', filename='templates/universities/gc.html') }}" },
    { name: 'Holy Angel University', url: "{{ url_for('static', filename='templates/universities/hau.html') }}" },
    { name: 'Mabalacat City College', url: "{{ url_for('static', filename='templates/universities/mcc.html') }}" },
    { name: 'Pampanga State Agricultural University', url: "{{ url_for('static', filename='templates/universities/psau.html') }}" },
    { name: 'Philippine Merchant Marine Academy', url: "{{ url_for('static', filename='templates/universities/pmma.html') }}" },
    { name: 'Ramon Magsaysay Technological University', url: "{{ url_for('static', filename='templates/universities/rmtu.html') }}" },
    { name: 'Tarlac Agricultural University', url: "{{ url_for('static', filename='templates/universities/tau.html') }}" },
    { name: 'Tarlac College of Agriculture', url: "{{ url_for('static', filename='templates/universities/tca.html') }}" },
    { name: 'Tarlac State University', url: "{{ url_for('static', filename='templates/universities/tsu.html') }}" },
    { name: 'University of the Assumption', url: "{{ url_for('static', filename='templates/universities/ua.html') }}" }
  ];

  searchButton.addEventListener('click', function () {
    const searchTerm = searchInput.value.trim().toLowerCase();
    
    // Filter schools based on search term
    const filteredSchools = schools.filter(school => school.name.toLowerCase().includes(searchTerm));
    
    if (searchTerm !== '' && filteredSchools.length > 0) {
      resultBox.style.display = 'block';
      // Display search results as links
      resultBox.innerHTML = filteredSchools.map(school => `<a href="${school.url}" class="result-item">${school.name}</a>`).join('');
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

document.addEventListener('DOMContentLoaded', function () {
  const gradientContainer = document.querySelector('.user .gradient-container');
  const dropdownMenu = document.querySelector('.user .dropdown-menu');

  gradientContainer.addEventListener('click', function () {
    if (dropdownMenu.style.display === 'block') {
      dropdownMenu.style.display = 'none';
    } else {
      dropdownMenu.style.display = 'block';
    }
  });

  // Hide dropdown when clicking outside of it
  document.addEventListener('click', function (event) {
    if (!gradientContainer.contains(event.target) && !dropdownMenu.contains(event.target)) {
      dropdownMenu.style.display = 'none';
    }
  });
});

document.addEventListener('DOMContentLoaded', function () {
    const monthNameElement = document.querySelector('.month-name');
    const daysContainer = document.querySelector('.days');
    const modal = document.querySelector('.event-modal');
    const addEventBtn = document.querySelector('#addEventBtn');
    const closeModalBtn = document.querySelector('.close-modal');
    const saveEventBtn = document.querySelector('#save-event-btn');
    const eventInputName = document.querySelector('#event-name');
    const eventInputDate = document.querySelector('#event-date');
    const eventInputTime = document.querySelector('#event-time');
    const eventInputDescription = document.querySelector('#event-description');
  
    let currentMonth = new Date().getMonth(); // Current month index (0 = January)
    let currentYear = new Date().getFullYear(); // Current year
  
    // Initial display of the month
    displayMonth(currentMonth, currentYear);
  
    // Function to display the month
    function displayMonth(month, year) {
      const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'];
  
      monthNameElement.textContent = `${monthNames[month]} ${year}`;
      renderCalendar(month, year);
    }
  
    // Click event for previous month button
    document.querySelector('.prev-month').addEventListener('click', function () {
      currentMonth--;
      if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
      }
      displayMonth(currentMonth, currentYear);
    });
  
    // Click event for next month button
    document.querySelector('.next-month').addEventListener('click', function () {
      currentMonth++;
      if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
      }
      displayMonth(currentMonth, currentYear);
    });
  
    // Function to render calendar for given month and year
    function renderCalendar(month, year) {
      const firstDay = new Date(year, month, 1).getDay(); // Day of the week (0-6) of the 1st day of the month
      const daysInMonth = new Date(year, month + 1, 0).getDate(); // Total days in the month
  
      // Clear previous month's days
      daysContainer.innerHTML = '';
  
      // Render weekdays
      const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      weekdays.forEach(day => {
        const weekdayElement = document.createElement('div');
        weekdayElement.textContent = day;
        daysContainer.appendChild(weekdayElement);
      });
  
      // Render days
      for (let i = 0; i < firstDay; i++) {
        const emptyDayElement = document.createElement('div');
        emptyDayElement.classList.add('day', 'empty');
        daysContainer.appendChild(emptyDayElement);
      }
  
      for (let day = 1; day <= daysInMonth; day++) {
        const dayElement = document.createElement('div');
        dayElement.textContent = day;
        dayElement.classList.add('day');
        dayElement.setAttribute('data-day', day);
        daysContainer.appendChild(dayElement);
  
        // Add click event to each day
        dayElement.addEventListener('click', function () {
          const eventDate = `${year}-${padNumber(month + 1)}-${padNumber(day)}`;
          if (dayElement.classList.contains('event-day')) {
            showEventDetails(eventDate);
          } else {
            eventInputDate.value = eventDate;
            modal.style.display = 'block';
          }
        });
      }
  
      // Load and mark events from localStorage
      loadEventsFromLocalStorage(month, year);
    }
  
    // Function to pad single digit numbers with leading zeros (e.g., 1 becomes '01')
    function padNumber(number) {
      return number.toString().padStart(2, '0');
    }
  
    // Close modal
    closeModalBtn.addEventListener('click', function () {
      modal.style.display = 'none';
    });
  
    // Save event
    saveEventBtn.addEventListener('click', function () {
      const eventName = eventInputName.value.trim();
      const eventDate = eventInputDate.value;
      let eventTime = eventInputTime.value;
      const eventDescription = eventInputDescription.value.trim();
  
      if (eventName && eventDate && eventTime) {
        // Format time to AM/PM
        eventTime = formatTimeToAMPM(eventTime);
  
        // Create event object
        const event = {
          name: eventName,
          date: eventDate,
          time: eventTime,
          description: eventDescription
        };
  
        // Save event to calendar and localStorage
        saveEventToCalendar(event);
  
        // Close modal
        modal.style.display = 'none';
  
        // Reset input fields
        eventInputName.value = '';
        eventInputDate.value = '';
        eventInputTime.value = '';
        eventInputDescription.value = '';
      } else {
        alert('Please fill in all required fields.');
      }
    });
  
    // Function to save event to calendar and localStorage
    function saveEventToCalendar(event) {
      const eventDay = parseInt(event.date.split('-')[2]);
      const eventMonth = parseInt(event.date.split('-')[1]) - 1;
      const eventYear = parseInt(event.date.split('-')[0]);
  
      // Retrieve existing events from localStorage or initialize an empty object if none exist
      let storedEvents = JSON.parse(localStorage.getItem('events')) || {};
  
      // Add the new event to the stored events object
      storedEvents[event.date] = event;
  
      // Save the updated events object back to localStorage
      localStorage.setItem('events', JSON.stringify(storedEvents));
  
      // Re-render the calendar to reflect the new event
      renderCalendar(currentMonth, currentYear);
    }
  
    // Function to load events from localStorage and mark them on the calendar
    function loadEventsFromLocalStorage(month, year) {
      const dayElements = document.querySelectorAll('.day');
      let storedEvents = JSON.parse(localStorage.getItem('events')) || {};
  
      Object.keys(storedEvents).forEach(eventDate => {
        const eventDay = parseInt(eventDate.split('-')[2]);
        const eventMonth = parseInt(eventDate.split('-')[1]) - 1;
        const eventYear = parseInt(eventDate.split('-')[0]);
  
        // Mark the event day on the calendar if the event is in the specified month and year
        if (eventMonth === month && eventYear === year) {
          dayElements.forEach(dayElement => {
            const day = parseInt(dayElement.getAttribute('data-day'));
            if (day === eventDay) {
              dayElement.classList.add('event-day');
            }
          });
        }
      });
    }
  
    // Function to format time to AM/PM
    function formatTimeToAMPM(time) {
      const [hour, minute] = time.split(':');
      let period = 'AM';
      let formattedHour = parseInt(hour);
  
      if (formattedHour >= 12) {
        period = 'PM';
        if (formattedHour > 12) {
          formattedHour -= 12;
        }
      } else if (formattedHour === 0) {
        formattedHour = 12;
      }
  
      return `${formattedHour}:${minute} ${period}`;
    }
  
    // Function to show event details in a popup
    function showEventDetails(eventDate) {
      let storedEvents = JSON.parse(localStorage.getItem('events')) || {};
      const event = storedEvents[eventDate];
  
      if (event) {
        const eventDetailsModal = document.createElement('div');
        eventDetailsModal.classList.add('event-details-modal');
        eventDetailsModal.innerHTML = `
          <div class="event-details-content">
            <span class="close-event-details">&times;</span>
            <h2>${event.name}</h2>
            <p><strong>Date:</strong> ${event.date}</p>
            <p><strong>Time:</strong> ${event.time}</p>
            <p><strong>Description:</strong> ${event.description}</p>
            <button id="edit-event-btn">Edit</button>
            <button id="delete-event-btn">Delete</button>
          </div>
        `;
        document.body.appendChild(eventDetailsModal);
  
        // Close event details modal
        eventDetailsModal.querySelector('.close-event-details').addEventListener('click', function () {
          document.body.removeChild(eventDetailsModal);
        });
  
        // Edit event
        eventDetailsModal.querySelector('#edit-event-btn').addEventListener('click', function () {
          document.body.removeChild(eventDetailsModal);
          eventInputName.value = event.name;
          eventInputDate.value = event.date;
          eventInputTime.value = event.time;
          eventInputDescription.value = event.description;
          modal.style.display = 'block';
        });
  
        // Delete event
        eventDetailsModal.querySelector('#delete-event-btn').addEventListener('click', function () {
          if (confirm('Do you want to delete this event?')) {
            deleteEvent(eventDate);
            document.body.removeChild(eventDetailsModal);
          }
        });
      }
    }
  
    // Function to delete event from localStorage and update the calendar
    function deleteEvent(eventDate) {
      let storedEvents = JSON.parse(localStorage.getItem('events')) || {};
      delete storedEvents[eventDate];
      localStorage.setItem('events', JSON.stringify(storedEvents));
      renderCalendar(currentMonth, currentYear);
    }
  });
  