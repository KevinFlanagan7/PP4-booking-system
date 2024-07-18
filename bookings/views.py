from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking
from .forms import BookingForm
from allauth.account.utils import user_email

def home_page(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }

    return render(request, 'bookings/index.html', context)
    

@login_required
def bookings_list(request):
    current_date = timezone.now().date()
    bookings = Booking.objects.filter(user=request.user, date__gte=current_date)
    return render(request, 'bookings/my-bookings.html', {'bookings_list': bookings})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  
            booking.save()

            # Send booking confirmation email using Allauth's email system
            subject = 'Booking Confirmation'
            email_context = {
                'user': request.user,
                'booking': booking,
                'is_update': False
            }
            message = render_to_string('bookings/email-confirmation.html', email_context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email]
            send_mail(subject, '', from_email, recipient_list, html_message=message)

            messages.success(request, 'Booking created successfully! Confirmation email sent!')
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

            # Send booking update confirmation email using Allauth's email system
            subject = 'Booking Updated'
            email_context = {
                'user': request.user,
                'booking': booking,
                'is_update': True
            }
            message = render_to_string('bookings/email-confirmation.html', email_context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email]
            send_mail(subject, '', from_email, recipient_list, html_message=message)

            messages.success(request, 'Booking updated successfully! Confirmation email sent!')
            return redirect('bookings_list')  
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/form.html', {'form': form, 'form_type': 'update'})



