
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from users.views import UsersViewSet as usersview

route=DefaultRouter()
route.register('users',usersview,basename="userview")

urlpatterns = [
 
  
    path('',include(route.urls))
]
