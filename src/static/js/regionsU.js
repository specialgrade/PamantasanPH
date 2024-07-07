document.addEventListener("DOMContentLoaded", function() {
    var bookmarkButtons = document.querySelectorAll(".bookmark-btn");

    bookmarkButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var universityCard = button.closest(".university-card");

            // Store the entire HTML content of the university card
            var universityHTML = universityCard.outerHTML;

            // Retrieve existing bookmarks from local storage
            var bookmarks = JSON.parse(localStorage.getItem('bookmarks')) || [];

            // Check if the university is already bookmarked
            var isBookmarked = bookmarks.some(function(bookmark) {
                return bookmark === universityHTML;
            });

            if (!isBookmarked) {
                // Add to bookmarks
                bookmarks.push(universityHTML);
                localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
                alert("University bookmarked!");
            } else {
                alert("University already bookmarked!");
            }
        });
    });
});