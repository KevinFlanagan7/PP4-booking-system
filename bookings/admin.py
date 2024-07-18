from django.contrib import admin
from .models import Booking
from allauth.socialaccount.models import SocialAccount, SocialApp, \
    SocialToken


# Registers Booking model with admin site
admin.site.register(Booking)

# Unregisters Social Account, App and Token with admin site
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)

