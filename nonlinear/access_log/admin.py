from django.contrib import admin
from .models import AccessLog

# Register your models here.


class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'data', 'ip_address', 'timestamp')


admin.site.register(AccessLog, AccessLogAdmin)
