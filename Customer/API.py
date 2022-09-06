
from datetime import date,timedelta,datetime
from rest_framework import serializers
from .models import Customer,Membership


class MembershipSerializer(serializers.ModelSerializer):

               class Meta:
                              model=Membership
                              fields="__all__"

class UsersSerializer(serializers.ModelSerializer):
               duration=serializers.SerializerMethodField(read_only=True)
               membership=MembershipSerializer 
               def get_duration(self,customer:Customer):
                  currentDate=date.today()
                  ex_datestr=str(datetime.strptime(str(customer.expire_date),'%Y-%m-%d').date()-currentDate).split(' ',1)[0]
                  if int(ex_datestr) <=0:
                     Customer.objects.update(is_active="INACTIVE")
                     return"renew your account"
                  else:
                     return  ex_datestr+" Days"  
               class Meta:
                 model=Customer
                 fields=['username','password','is_active','membership',"start_date","expire_date",'duration']