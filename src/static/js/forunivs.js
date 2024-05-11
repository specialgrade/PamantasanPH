document.addEventListener("DOMContentLoaded", function() {
    var bookmarkIcons = document.querySelectorAll(".bookmark-icon");

    bookmarkIcons.forEach(function(icon) {
        icon.addEventListener("click", function() {
            var container = icon.closest(".bg-container");
            var containerHTML = container.outerHTML;

            var bookmarkedContent = localStorage.getItem('bookmarkedContent');
            if (!bookmarkedContent) {
                bookmarkedContent = [];
            } else {
                bookmarkedContent = JSON.parse(bookmarkedContent);
            }

            if (bookmarkedContent.includes(containerHTML)) {
                alert("Already Bookmarked!");
                return;
            }

            bookmarkedContent.push(containerHTML);
            localStorage.setItem('bookmarkedContent', JSON.stringify(bookmarkedContent));

            alert("Click 'OK' to Add to Bookmarks.");
        });
    });
});