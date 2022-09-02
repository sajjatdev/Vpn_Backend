from django.db import models
from datetime import date,datetime




class Membership(models.Model):
               name=[("Day","Day"),("Month","Month"),("Years","Years")]
               duration=models.PositiveIntegerField()
               name=models.CharField(choices=name,default="DY",max_length=255)
               def __str__(self):
                              return str(self.duration) +" " +self.name

               class Meta:
                              db_table = 'membership'
                              managed = True
                             
               

class Customer(models.Model):
               IS_ACTIVE=[("ACTIVE",'Active'),("INACTIVE","Inactive")]
               username=models.CharField(unique=True,max_length=255)
               password=models.CharField(max_length=255)
               is_active=models.CharField(choices=IS_ACTIVE,default="ACTIVE",max_length=255)
               start_date=models.DateTimeField(auto_now=True)
               membership=models.ForeignKey(Membership,on_delete=models.CASCADE,related_name="membership")
               duration=models.DateField(default=date.today)
               def __str__(self):
                            return  self.username

               class Meta:
                              db_table = 'customer'
                              managed = True
                        
               @property
               def membershipday(self):
                              currentDate=date.today()
                              ex_datestr=str(datetime.strptime(str(self.duration),'%Y-%m-%d').date()-currentDate).split(' ',1)[0]
                              
                              if ex_datestr=="0":
                                     instance= Customer.objects.filter(pk=self.id).update(is_active="INACTIVE")    
                                     instance.save()        
                                     return "you Need to Renew"              
                              return ex_datestr 