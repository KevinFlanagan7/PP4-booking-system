from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

def home_page(request):

    return render(request, 'bookings/index.html')
    

@login_required
def bookings_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_detail.html', {'object_list': bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()
            return redirect('bookings_list')  
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('bookings_list')  
    return render(request, 'bookings/delete_booking.html', {'booking': booking})

@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')  
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/update_booking.html', {'form': form})



