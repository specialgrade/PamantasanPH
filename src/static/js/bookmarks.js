// Bookmark function
document.addEventListener("DOMContentLoaded", function() {
    var favsContainer = document.getElementById('favsContainer');

    var bookmarkedContent = localStorage.getItem('bookmarkedContent');
    if (bookmarkedContent) {
        bookmarkedContent = JSON.parse(bookmarkedContent);
        bookmarkedContent.forEach(function(content) {
            var div = document.createElement('div');
            div.innerHTML = content;

            var bookmarkIcon = div.querySelector('.bookmark-icon');  
            bookmarkIcon.addEventListener('click', function() {
                 
                var confirmation = confirm("Click 'OK' to Remove from Bookmarks.");
                if (confirmation) {
                    favsContainer.removeChild(div);

                    var index = bookmarkedContent.indexOf(content);
                    if (index !== -1) {
                        bookmarkedContent.splice(index, 1);
                        localStorage.setItem('bookmarkedContent', JSON.stringify(bookmarkedContent));
                    }
                }
            });

            favsContainer.appendChild(div);
        });
    }
});

// Displayed text when the container is empty
function checkEmptyContainer() {
    var bookmarkedContent = localStorage.getItem('bookmarkedContent');
    var favsContainer = document.getElementById('favsContainer');

    if (!bookmarkedContent || JSON.parse(bookmarkedContent).length === 0) {
        favsContainer.innerHTML = '<p class="bookmarks-text">Add your bookmarks here</p>';
    } else {
        favsContainer.innerHTML = ''; 
    }
}