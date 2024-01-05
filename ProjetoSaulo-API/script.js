document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'http://127.0.0.1:8000/adotante/'; // Replace with your API endpoint URL

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ${response.status}');
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // Print the response to the console
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
});

// Modelo de request com JS para o back