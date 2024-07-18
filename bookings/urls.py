from . import views
from django.urls import path
from .views import bookings_list

urlpatterns = [
    # Homepage
    path('', views.home_page, name='home'),
    # List all bookings
    path('bookings/', bookings_list, name='bookings_list'),
    # Create a new booking
    path('bookings/new/', views.create_booking, name='create_booking'),
    # Delete a booking by booking_id
    path(
        'bookings/<int:booking_id>/delete_booking/',
        views.delete_booking, name='delete_booking'
        ),
    # Update a booking by booking_id
    path(
        'bookings/<int:booking_id>/update/',
        views.update_booking, name='update_booking'
        ),
]
