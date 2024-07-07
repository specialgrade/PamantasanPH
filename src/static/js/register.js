document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').addEventListener('click', function (event) {
        event.preventDefault();

        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const agree = document.getElementById('agree').checked;

        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        if (!agree) {
            alert("You must agree to the privacy policy.");
            return;
        }

        fetch('{{ url_for("register") }}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                firstName: firstName,
                lastName: lastName,
                email: email,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = '{{ url_for("login") }}';
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
