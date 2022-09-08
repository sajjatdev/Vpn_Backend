
from dataclasses import field
from datetime import date,timedelta,datetime
from rest_framework import serializers
from .models import Customer,Membership,Reseller


class MembershipSerializer(serializers.ModelSerializer):

               class Meta:
                              model=Membership
                              fields="__all__"

class UsersSerializer(serializers.ModelSerializer):
               duration=serializers.SerializerMethodField(read_only=True)
               expire_date=serializers.DateField(read_only=True)
               membership=MembershipSerializer 
              
               class Meta:
                 model=Customer
                 fields=['username','password','is_active','membership',"start_date","expire_date",'reseller','duration']

               def get_duration(self,customer:Customer):
                  currentDate=date.today()
                  ex_datestr=str(datetime.strptime(str(customer.expire_date),'%Y-%m-%d').date()-currentDate).split(' ',1)[0]
                  if int(ex_datestr) <=0:
                     Customer.objects.update(is_active="INACTIVE")
                     return"renew your account"
                  else:
                      return  ex_datestr+" Days"


class ReSellerSerializer(serializers.ModelSerializer):
         uid=serializers.UUIDField(read_only=True)
         class Meta:
            model=Reseller
            fields=['uid','username','password','status',"create_at","isadmin","status",'credit']