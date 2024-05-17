from django.contrib import admin
from .models import Booking, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('user', 'created_on')
    list_filter = ('user',)
    summernote_fields = ('comment',)

# Register your models here.
admin.site.register(Booking)

