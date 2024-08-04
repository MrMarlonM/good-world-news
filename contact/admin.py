from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Contact model.
    """
    list_display = ('reason', 'name', 'created_on')
    list_filter = ('reason', 'created_on')