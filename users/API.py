from dataclasses import field
from rest_framework import serializers
from .models import Customer,Membership


class MembershipSerializer(serializers.ModelSerializer):

               class Meta:
                              model=Membership
                              fields="__all__"

class UsersSerializer(serializers.ModelSerializer):
               duration=serializers.DateField(read_only=True)
               membership=MembershipSerializer
               class Meta:
                 model=Customer
                 fields=['username','password','is_active','membership',"start_date","membershipday",'duration']