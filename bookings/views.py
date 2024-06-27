from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

def home_page(request):

    return render(request, 'bookings/index.html')
    

@login_required
def bookings_list(request):
    current_date = timezone.now().date()
    bookings = Booking.objects.filter(user=request.user, date__gte=current_date)
    return render(request, 'bookings/list.html', {'bookings_list': bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('bookings_list')  
    else:
        form = BookingForm()
    return render(request, 'bookings/form.html', {'form': form, 'form_type': 'create'})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking has been deleted successfully.')
        return redirect('bookings_list')  
    return redirect('bookings_list')

@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('bookings_list')  
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/form.html', {'form': form, 'form_type': 'update'})



