document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').addEventListener('click', function (event) {
        event.preventDefault();

        const email = document.getElementById('email').value;

        fetch('{{ url_for("reset_password") }}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Verification card sent to your email.");
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
