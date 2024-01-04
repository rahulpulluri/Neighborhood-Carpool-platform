 function showEditForm() {
        var carpoolDetails = document.querySelector('.carpool-details');
        var h2 = document.querySelector('h2');
        var pTags = document.querySelectorAll('p');
        var editForm = document.querySelector('.edit-form');

        // Hide the h2 and p elements
        h2.style.display = 'none';
        pTags.forEach(function (p) {
            p.style.display = 'none';
        });

        // Display the edit form
        editForm.style.display = 'block';
    }

    function confirmDelete() {
        if (confirm('Are you sure you want to delete this carpool?')) {
            var carpoolDetails = document.querySelector('.carpool-details');
            var h2 = document.querySelector('h2');
            var pTags = document.querySelectorAll('p');
            var editForm = document.querySelector('.edit-form');

            // Hide the h2 and p elements
            h2.style.display = 'none';
            pTags.forEach(function (p) {
                p.style.display = 'none';
            });

            alert('Carpool deleted successfully.');

            // Hide the edit form and show the carpool details
            editForm.style.display = 'none';
            carpoolDetails.style.display = 'block';
        }
    }

    function saveForm() {
        alert('Carpool details saved successfully.');
        var editForm = document.querySelector('.edit-form');
        editForm.style.display = 'none';
        var carpoolDetails = document.querySelector('.carpool-details');
        carpoolDetails.style.display = 'block';
    }

    // Hides the edit form when the page loads
    window.onload = function () {
        var editForm = document.querySelector('.edit-form');
        editForm.style.display = 'none';
    }