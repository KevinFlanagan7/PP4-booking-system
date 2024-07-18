from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Model of a booking made by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns a string indicating the user who made the booking.
        """
        return f"Booking by {self.user}"
