from django_filters.rest_framework import FilterSet
from . import models
class ResellerFilter(FilterSet):
    class Meta:
        model = models.Reseller
        fields = {'uid':['exact'],'username':['exact'], 'password':['exact'], 'status':['exact'], 'create_admin':['exact']}

