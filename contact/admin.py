from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('reason', 'name', 'created_on')
    list_filter = ('reason', 'created_on')