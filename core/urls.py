
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Customer   import views  as customerview

route=DefaultRouter()
route.register('customer',customerview.UsersViewSet,basename="userview")
route.register("Membership",customerview.MembershipViewSet,basename='membership')
route.register("reseller",customerview.ReSellerViewSet,basename="reseller"),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls))
]
