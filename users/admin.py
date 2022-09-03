from django.contrib import admin

from .models import Customer


admin.sites.AdminSite.site_header="VPN"
admin.sites.AdminSite.site_title="Online Vpn Buy Sell"
admin.sites.AdminSite.index_title="VPN"

class CustomerAdmin(admin.ModelAdmin):
               
               list_display=['username','password','is_active','membership']

admin.site.register(Customer,CustomerAdmin)

