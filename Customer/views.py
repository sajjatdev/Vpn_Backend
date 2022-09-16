
from datetime import date, timedelta
from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework import pagination
from .API import UsersSerializer, ReSellerSerializer, MembershipSerializer, ReSellerStatus
from .models import Customer, Membership, Reseller, ResellerOnlineStatus
from .filtes import ResellerFilter


class UsersViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return Customer.objects.all()

    def create(self, request, *args, **kwargs):
        user_date = request.data
        validator = Customer.objects.filter(
            Q(username=user_date["username"])).all()
        if not validator:
            duration_count = Membership.objects.get(pk=user_date['membership'])
            print(duration_count.name)
            if duration_count.name == "Month":
                user_model = Customer.objects.create(username=user_date['username'], password=user_date['password'], is_active=user_date['is_active'], reseller_id=user_date[
                                                     'reseller'], membership_id=user_date['membership'], expire_date=(date.today()+timedelta(days=30*duration_count.duration)).isoformat())
                serializer = UsersSerializer(user_model)
                return Response(serializer.data)
            elif duration_count.name == "Years":
                user_model = Customer.objects.create(username=user_date['username'], password=user_date['password'], is_active=user_date['is_active'], membership_id=user_date[
                                                     'membership'], reseller_id=user_date['reseller'], expire_date=(date.today()+timedelta(days=365*duration_count.duration)).isoformat())
                serializer = UsersSerializer(user_model)
                return Response(serializer.data)
            elif duration_count.name == "Day":
                user_model = Customer.objects.create(username=user_date['username'], password=user_date['password'], is_active=user_date['is_active'], membership_id=user_date[
                                                     'membership'], reseller_id=user_date['reseller'], expire_date=(date.today()+timedelta(days=duration_count.duration)).isoformat())
                serializer = UsersSerializer(user_model)
                return Response(serializer.data)
        else:
            return Response({"Error": "This item already exists"}, status=status.HTTP_303_SEE_OTHER)


class ReSellerViewSet(ModelViewSet):
    queryset = Reseller.objects.all()
    serializer_class = ReSellerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ResellerFilter
    search_fields = ['username']


class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class SellerStatusViewSet(ModelViewSet):
    queryset = ResellerOnlineStatus.objects.all()
    serializer_class = ReSellerStatus
