
from datetime import date,timedelta
from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import pagination 
from .API import UsersSerializer
from .models import Customer,Membership





class UsersViewSet(ModelViewSet):
          
               serializer_class=UsersSerializer
               pagination_class=pagination.PageNumberPagination
               def get_queryset(self):

                       return Customer.objects.all()


               def create(self, request, *args, **kwargs):
                       user_date=request.data
                       validator=Customer.objects.filter(Q(username=user_date["username"])).all()
                       if not validator :
                              duration_count=Membership.objects.get(pk=user_date['membership'])
                              print(duration_count.name)
                              if duration_count.name == "Month" :
                                   user_model= Customer.objects.create(username=user_date['username'],password=user_date['password'],is_active=user_date['is_active'],membership_id=user_date['membership'],duration= (date.today()+timedelta(days=30*duration_count.duration)).isoformat()  )      
                                   serializer=UsersSerializer(user_model)
                                   return Response(serializer.data)
                              elif  duration_count.name == "Years":
                                   user_model= Customer.objects.create(username=user_date['username'],password=user_date['password'],is_active=user_date['is_active'],membership_id=user_date['membership'],duration= (date.today()+timedelta(days=365*duration_count.duration)).isoformat()  )      
                                   serializer=UsersSerializer(user_model)
                                   return Response(serializer.data)  
                              elif  duration_count.name == "Day":
                                   user_model= Customer.objects.create(username=user_date['username'],password=user_date['password'],is_active=user_date['is_active'],membership_id=user_date['membership'],duration= (date.today()+timedelta(days=duration_count.duration)).isoformat()  )      
                                   serializer=UsersSerializer(user_model)
                                   return Response(serializer.data)                           
                       else:
                              return Response({"Error":"This item already exists"},status=status.HTTP_303_SEE_OTHER)   

               def partial_update(self, request, *args, **kwargs):
                       return super().partial_update(request, *args, **kwargs)

                       


                   