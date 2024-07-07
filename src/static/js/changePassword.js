document.addEventListener('DOMContentLoaded', () => {
    const changePasswordForm = document.getElementById('change-password-form');
    changePasswordForm.addEventListener('submit', (event) => {
        event.preventDefault();
        changePasswordForm.submit();
    });
});
