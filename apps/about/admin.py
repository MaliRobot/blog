from django.contrib import admin
from .models import About, Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'message')


admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
