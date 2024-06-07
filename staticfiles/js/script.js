console.log("Life, The Universe and Everything!");

document.addEventListener("DOMContentLoaded", function() {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const deleteForm = document.getElementById("deleteForm");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(e) {
            let bookingId = e.target.getAttribute("booking_id");
            deleteForm.action = `/bookings/${bookingId}/delete_booking/`;
            deleteModal.show();
        });
    });
});