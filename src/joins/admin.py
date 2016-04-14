from django.contrib import admin
from .models import Join


# Register your models here.

class JoinAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','email','ip_address','timestamp','updated','ref_id','friends']
    class Meta:
        model = Join


admin.site.register(Join, JoinAdmin)

#admin.site.register(JoinFriends)