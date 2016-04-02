from django.contrib import admin
from .models import Join


# Register your models here.

class JoinAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','email','timestamp','updated']
    class Meta:
        model = Join


admin.site.register(Join, JoinAdmin)
