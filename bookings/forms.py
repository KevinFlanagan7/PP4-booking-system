from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from datetime import time, timedelta, datetime


def generate_time_slots(start_time, end_time, interval):
    """
    Generates time slots between 9am and 5pm with 1 hour interval.
    Does not include 1pm for lunch.
    """
    slots = []
    current_time = datetime.combine(datetime.today(), start_time)
    end_time = datetime.combine(datetime.today(), end_time)
    while current_time <= end_time:
        if current_time.time() != time(13, 0):
            slots.append((current_time.time(), current_time.strftime("%H:%M")))
        current_time += interval
    return slots


TIME_CHOICES = generate_time_slots(time(9, 0), time(17, 0), timedelta(hours=1))


class BookingForm(forms.ModelForm):
    """
    Form for booking date and time slot.
    """
    date = forms.DateField(
        label="Select Date",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    time = forms.ChoiceField(
        label="Select Time",
        choices=TIME_CHOICES
    )

    class Meta:
        model = Booking
        fields = ['date', 'time']

    def clean_date(self):
        """
        Validates selected date to ensure it's not in the past or on weekends.
        """
        selected_date = self.cleaned_data['date']
        today = datetime.today().date()
        if selected_date < today:
            raise ValidationError("You cannot book a date in the past.")

        if selected_date.weekday() >= 5:
            raise ValidationError(
                "You can only book dates from Monday to Friday."
                )

        return selected_date

    def clean(self):
        """
        Validates that the selected date and time slot is available.
        """
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time:
            if Booking.objects.filter(date=date, time=time).exists():
                raise ValidationError(
                    "This date and time slot has already been booked."
                    )

        return cleaned_data
