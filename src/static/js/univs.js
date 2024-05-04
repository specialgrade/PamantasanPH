// status [WILL FINALIZE]
const statusIcon = document.getElementById('status-icon');
const statusText = document.getElementById('status-text');

if (document.getElementById('status').textContent === 'NOT YET OPENED') {
	statusIcon.classList.remove('open');
	statusText.textContent = 'NOT YET OPENED';
} else {
	statusIcon.classList.add('open');
	statusText.textContent = 'OPEN';
}