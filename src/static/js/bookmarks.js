document.addEventListener("DOMContentLoaded", function() {
    var favsContainer = document.getElementById('favsContainer');
    var placeholderText = document.getElementById('placeholderText');

    // Retrieve bookmarks from local storage
    var bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];

    // Generate or update bookmarks display
    if (bookmarks.length > 0) {
        placeholderText.style.display = 'none';
        bookmarks.forEach(function(bookmarkHTML, index) {
            // Create a div for each bookmarked university card
            var div = document.createElement('div');
            div.classList.add('bookmark-container');  

            div.innerHTML = bookmarkHTML; // Assign the stored HTML content

            // Create remove button
            var removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.classList.add('remove-btn', 'button-style');  

            // Add event listener to remove button
            removeButton.addEventListener('click', function() {
                // Remove the div from DOM
                favsContainer.removeChild(div);

                // Remove the bookmark from local storage
                bookmarks.splice(index, 1);
                localStorage.setItem('bookmarks', JSON.stringify(bookmarks));

                // Show placeholder text if there are no bookmarks left
                if (bookmarks.length === 0) {
                    placeholderText.style.display = 'block';
                }

                // Display confirmation message
                alert("University removed!");
            });

            // Append remove button to the bookmark container
            div.appendChild(removeButton);

            // Append the div to favsContainer
            favsContainer.appendChild(div);
        });
    } else {
        placeholderText.style.display = 'block';
    }

    // Function to display confirmation message
    function displayConfirmation(message) {
        // Create a confirmation message element
        var confirmationMsg = document.createElement('div');
        confirmationMsg.textContent = message;
        confirmationMsg.classList.add('confirmation-msg');  

        document.body.appendChild(confirmationMsg);

        setTimeout(function() {
            document.body.removeChild(confirmationMsg);
        }, 3000);  
    }
});

