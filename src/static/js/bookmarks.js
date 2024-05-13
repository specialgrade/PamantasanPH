document.addEventListener("DOMContentLoaded", function() {
    var favsContainer = document.getElementById('favsContainer');
    var placeholderText = document.getElementById('placeholderText');

    var bookmarkedContent = localStorage.getItem('bookmarkedContent');
    if (bookmarkedContent) {
        bookmarkedContent = JSON.parse(bookmarkedContent);
        bookmarkedContent.forEach(function(content) {
            var div = document.createElement('div');
            div.innerHTML = content;
            div.classList.add('bookmark-container'); // Adding a class for styling

            var unbookmarkButton = document.createElement('button');
            unbookmarkButton.textContent = 'Unbookmark';
            unbookmarkButton.classList.add('unbookmark', 'button-style'); // Adding a class for button styling

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
