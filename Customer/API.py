
from datetime import date, timedelta, datetime
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .exception import MyCustomExcpetion
from .models import Customer, Membership, Reseller, ResellerOnlineStatus


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField(read_only=True)
    expire_date = serializers.DateField(read_only=True)
    membership = MembershipSerializer

    class Meta:
        model = Customer
        fields = ['username', 'password', 'is_active', 'membership',
                  "start_date", "expire_date", 'reseller', 'duration']

    def get_duration(self, customer: Customer):
        currentDate = date.today()
        ex_datestr = str(datetime.strptime(
            str(customer.expire_date), '%Y-%m-%d').date()-currentDate).split(' ', 1)[0]
        if int(ex_datestr) <= 0:
            Customer.objects.update(is_active="INACTIVE")
            return "renew your account"
        else:
            return ex_datestr+" Days"


class ReSellerStatus (serializers.ModelSerializer):
    class Meta:
        model = ResellerOnlineStatus
        fields = "__all__"


class ReSellerSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Reseller
        fields = ['uid', 'username', 'password', "create_admin",
                  'status', "create_at", "isadmin", "status", 'credit']

    def create(self, validated_data):
        admindata = admindata = Reseller.objects.get(
            pk=validated_data["create_admin"])
        if admindata.isadmin == False:
            if admindata.credit != 0:
                mainCredit = int(admindata.credit - validated_data["credit"])
                admindata.credit = mainCredit
                admindata.save()

                return super().create(validated_data)
            else:
                adminstatus = ResellerOnlineStatus.objects.get(
                    pk=validated_data["create_admin"])
                adminstatus.status = False
                adminstatus.save()
                admindata.status = "Inactive"
                admindata.save()
                raise MyCustomExcpetion(
                    detail={"Message": "you need add credit in your account"}, status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            return super().create(validated_data)
