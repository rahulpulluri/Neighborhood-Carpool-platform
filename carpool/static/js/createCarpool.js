$(document).ready(function() {
    // $("#modal-container").css("display", "none");
    // Event: Click event on the "Add Carpool" button
    $("#submit-button").click(function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Retrieve form data
        var carModel = $("#fname").val().trim();
        var departureTime = $("#departure-time").val().trim();
        var arrivalTime = $("#arrival-time").val().trim();
        var route = $("#Rname").val().trim();
        var availableSeats = $("#Aseats").val();

        // Perform form validation
        if (carModel === "" || departureTime === "" || arrivalTime === "" || route === "" || availableSeats <= 0) {
            alert("Please fill out all required fields and ensure that Available Seats is a positive number.");
            return; // Exit the function if validation fails
        }

        // If form validation passes, show the modal dialog
        $("#modal-container").css("display", "block");

        // You can add further logic here to send the data to your server or perform other actions.

        // Clear the form fields
        $("#carpool-form")[0].reset();
    });

    // Event: Click event on the modal's close button
    $("#modal-close-button, .modal").click(function() {
        $("#modal-container").css("display", "none");
    });
});
