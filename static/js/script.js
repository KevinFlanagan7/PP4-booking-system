document.addEventListener("DOMContentLoaded", function() {
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const deleteForm = document.getElementById("deleteForm");

    if (deleteModalElement && deleteForm && deleteButtons) {
        const deleteModal = new bootstrap.Modal(deleteModalElement);
        deleteButtons.forEach(button => {
            button.addEventListener("click", function(e) {
                let bookingId = e.target.getAttribute("booking_id");
                deleteForm.action = `/bookings/${bookingId}/delete_booking/`;
                deleteModal.show();
            });
        });
    }
});