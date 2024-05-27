from . import views
from django.urls import path
from .views import bookings_list

urlpatterns = [
    path('', views.home_page, name='home'),
    path('bookings/', bookings_list, name='bookings_list'),
    path('bookings/new/', views.create_booking, name='create_booking'),
    path('bookings/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('bookings/<int:booking_id>/update/', views.update_booking, name='update_booking'), 
]