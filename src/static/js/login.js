document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');

    const loginForm = document.getElementById('login-form');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        console.log('Form submission intercepted');

        const email = document.querySelector('input[name="email"]').value;
        const password = document.querySelector('input[name="password"]').value;
        const remember = document.querySelector('input[name="remember"]').checked;

        console.log('Form data:', { email, password, remember });

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password,
                remember: remember
            })
        })
        .then(response => {
            console.log('Response status:', response.status);
            return response.json();
        })
        .then(data => {
            console.log('Response from server:', data);
            if (data.success) {
                window.location.href = '/dashboard';
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
