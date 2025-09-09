from django.contrib import admin
from .models import Poem
# Register your models here.


class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')


admin.site.register(Poem, PoemAdmin)

