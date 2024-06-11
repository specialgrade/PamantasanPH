<<<<<<< HEAD
// Bookmark function
document.addEventListener("DOMContentLoaded", function() {
    var favsContainer = document.getElementById('favsContainer');
=======
// Unbookmark
document.addEventListener("DOMContentLoaded", function() {
    var favsContainer = document.getElementById('favsContainer');
    var placeholderText = document.getElementById('placeholderText');
>>>>>>> 32009e5584ac9f93a7bc2c4ad3181539d5d9ffc9

    var bookmarkedContent = localStorage.getItem('bookmarkedContent');
    if (bookmarkedContent) {
        bookmarkedContent = JSON.parse(bookmarkedContent);
        bookmarkedContent.forEach(function(content) {
            var div = document.createElement('div');
            div.innerHTML = content;
<<<<<<< HEAD

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
=======
            div.classList.add('bookmark-container');  

            var unbookmarkButton = document.createElement('button');
            unbookmarkButton.textContent = 'Unbookmark';
            unbookmarkButton.classList.add('unbookmark', 'button-style');  

            unbookmarkButton.addEventListener('click', function() {
                favsContainer.removeChild(div);

                var index = bookmarkedContent.indexOf(content);
                if (index !== -1) {
                    bookmarkedContent.splice(index, 1);
                    localStorage.setItem('bookmarkedContent', JSON.stringify(bookmarkedContent));
                }

                if (favsContainer.children.length === 0) {
                    placeholderText.style.display = 'block';
                }
            });

            div.appendChild(unbookmarkButton);

            favsContainer.appendChild(div);
        });
    } else {
        placeholderText.style.display = 'block';
    }
});
>>>>>>> 32009e5584ac9f93a7bc2c4ad3181539d5d9ffc9
