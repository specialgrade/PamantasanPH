// status [WILL FINALIZE]
const statusIcon = document.getElementById('status-icon');
const statusText = document.getElementById('status-text');

if (statusText.textContent === 'NOT YET OPENED') { 
	statusIcon.classList.remove('open');
} else {
	statusIcon.classList.add('open');
}