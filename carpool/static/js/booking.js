$(document).ready(function () {
  $('.increment').click(function () {
    // Get the carpool ID and AJAX URL from data attributes of the button
    var carpool_id = $(this).data('carpool-id');
    var ajax_url = $(this).data('ajax-url');

    $.ajax({
      url: ajax_url, // Send the request to the URL specified in the button's data-ajax-url attribute
      data: {
        'carpool_id': carpool_id // Send the carpool ID as data with the request
      },
      type: "POST", // Set method as POST
      dataType: "json", // Expect JSON response

      // Set the CSRF Token in the header for Django's CSRF protection
      headers: {'X-CSRFToken': csrftoken},

      context: this // Pass the button context for use in the callback
    })
    .done(function (json) {
      // If the request is successful and the server sends back a success response
      if (json.success == 'success') {
        // Find the nearest availableSeats div and update its text with the new seats count
        var availableSeatsDiv = $(this).closest('tr').find('div.availableSeats');
        var carpoolSeats = json.availableSeats;
        $(availableSeatsDiv).text(carpoolSeats);
      } else {
        // If the server sends back an error response, alert the error message
        alert('Error: ' + json.error);
      }
    })
    .fail(function (xhr, status, errorThrown) {
      // If the request fails, log the error and alert the user
      console.log("Error: " + errorThrown);
      console.log("Status: " + status);
      console.dir(xhr);
      alert("There was a problem with the request, please try again.");
    })
    .always(function () {
      // This code runs regardless of the Ajax request outcome
      console.log("The request is complete!");
    });
  });

 $('.decrement').click(function (){
        var carpool_id = $(this).data('carpool-id');
        var ajax_url = $(this).data('ajax-url-decrement'); // Ensure you have this data attribute in your HTML

        $.ajax({
            url: ajax_url,
            method: "POST",
            data: {
                carpool_id: carpool_id
            },
            dataType: "json",
            headers: {'X-CSRFToken': csrftoken},
            context: this
        })
        .done(function (json){
            if (json.success === 'success'){
                var availableSeatsDiv = $(this).closest('tr').find('td.availableSeats'); // Adjust if necessary
                var carpoolSeats = json.availableSeats;
                $(availableSeatsDiv).text(carpoolSeats);

                // Optionally, trigger a UI update or refresh if necessary
                availableSeatsDiv.trigger('change'); // If you have a handler that updates on 'change'
                // OR
                location.reload(); // As a last resort to force a refresh from server
            } else {
                alert('Error: ' + json.error);
            }
    })

    });
});


// Function to get the CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Get the CSRF token
const csrftoken = getCookie('csrftoken');
