from django.contrib import admin

from .models import Customer,Membership




class CustomerAdmin(admin.ModelAdmin):
               exclude= ('duration','expire_date',)
               list_display=['username','password','is_active','membership']
               
                       
admin.site.register(Customer,CustomerAdmin)

class MembershipAdmin(admin.ModelAdmin):
               pass
admin.site.register(Membership,MembershipAdmin)
