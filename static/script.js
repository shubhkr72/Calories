
document.getElementById('myForm').onsubmit = function () {
    // event.preventDefault(); // Stop the form from submitting
    showPopup();
};

// Function to display the popup
function showPopup() {
    const popup = document.getElementById('card');
    popup.style.display = 'flex'; // Show the popup
}

// Function to close the popup
function closePopup() {
    const popup = document.getElementById('card');
    popup.style.display = 'none'; // Hide the popup
}