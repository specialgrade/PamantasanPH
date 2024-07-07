document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.verify-btn').addEventListener('click', function (event) {
        event.preventDefault();

        const digit1 = document.querySelector('input[name="digit1"]').value;
        const digit2 = document.querySelector('input[name="digit2"]').value;
        const digit3 = document.querySelector('input[name="digit3"]').value;
        const digit4 = document.querySelector('input[name="digit4"]').value;

        const otp = digit1 + digit2 + digit3 + digit4;

        fetch('{{ url_for("verify_otp") }}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                otp: otp
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Email verified successfully.");
                window.location.href = '{{ url_for("dashboard") }}';
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
