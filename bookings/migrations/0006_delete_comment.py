# Generated by Django 4.2.11 on 2024-07-18 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_remove_booking_duration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]