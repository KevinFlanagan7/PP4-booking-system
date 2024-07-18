// Initialize the location map
function initMap() {
    const location = { lat: 53.33039343219796, lng: -8.15245492941211 };

    // Map centered at the location
    const map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 12,
        mapId: 'Golf Academy'
    });

     // Marker at the location
    new google.maps.marker.AdvancedMarkerElement({
        position: location,
        map: map,
        title: 'Ballinasloe Golf Academy & Driving Range'
    });
}

/**
 * This script sets up the delete modal functionality for booking deletions.
 * When the DOM content is fully loaded, it attaches event listeners
 * to all delete buttons, which will display a modal to delete booking_id.
 */
document.addEventListener("DOMContentLoaded", function () {
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const deleteForm = document.getElementById("deleteForm");

     // Ensure all elements exist before proceeding
    if (deleteModalElement && deleteForm && deleteButtons) {
        const deleteModal = new bootstrap.Modal(deleteModalElement);
        deleteButtons.forEach(button => {
            button.addEventListener("click", function (e) {
                let bookingId = e.target.getAttribute("booking_id");
                deleteForm.action = `/bookings/${bookingId}/delete_booking/`;
                deleteModal.show();
            });
        });
    }
});