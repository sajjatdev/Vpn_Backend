from django.db import models
from datetime import date,timedelta,datetime
from uuid import uuid4



class Membership(models.Model):
               name=[("Trial","Trial"),("Day","Day"),("Month","Month"),("Years","Years")]
               duration=models.PositiveIntegerField()
               name=models.CharField(choices=name,default="Trial",max_length=255)
               def __str__(self):
                              return str(self.duration) +" " +self.name

               class Meta:
                              db_table = 'membership'
                              managed = True
                             
class Reseller(models.Model):
       STATUS=[("Inactive","Inactive"),("Active","Active")]
       uid=models.UUIDField(primary_key=True,default=uuid4,unique=True)
       credit=models.PositiveIntegerField()
       isadmin=models.BooleanField(default=True)
       username=models.CharField(max_length=255,unique=True)
       password=models.CharField(max_length=255)
       status=models.CharField(choices=STATUS,default="Active",max_length=255)
       create_at=models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.username
       class Meta:
              db_table = 'reseller'
              managed = True
              verbose_name = 'Reseller'
              verbose_name_plural = 'Resellers'





class Customer(models.Model):
               IS_ACTIVE=[("ACTIVE",'Active'),("INACTIVE","Inactive")]
               reseller=models.ForeignKey(Reseller,on_delete=models.CASCADE,related_name="reseller")
               username=models.CharField(unique=True,max_length=255)
               password=models.CharField(max_length=255)
               is_active=models.CharField(choices=IS_ACTIVE,default="ACTIVE",max_length=255)
               start_date=models.DateTimeField(auto_now=True)
               membership=models.ForeignKey(Membership,on_delete=models.CASCADE,related_name="membership")
               expire_date=models.DateField(default=date.today)
               def __str__(self):
                            return  self.username

               class Meta:
                              db_table = 'customer'
                              managed = True

               def save(self, *args, **kwargs):
                              duration_count=Membership.objects.get(pk=self.membership.id)
                              if duration_count.name == "Month" :
                                     self.expire_date= (date.today()+timedelta(days=30*duration_count.duration)).isoformat()     
                                     super(Customer,self).save(*args,**kwargs)
                              elif  duration_count.name == "Years":
                                     self.expire_date= (date.today()+timedelta(days=365*duration_count.duration)).isoformat()     
                                     super(Customer,self).save(*args,**kwargs)
                              elif  duration_count.name == "Day" or duration_count.name == "Trial":
                                   self.expire_date= (date.today()+timedelta(days=duration_count.duration)).isoformat()     
                                   super(Customer,self).save(*args,**kwargs)
                     
              # Get Request Block Start
              
              #  @property
              #  def duration(self):
              #                 currentDate=date.today()
              #                 ex_datestr=str(datetime.strptime(str(self.expire_date),'%Y-%m-%d').date()-currentDate).split(' ',1)[0]
              #                 if int(ex_datestr)<=0:
              #                        instance= Customer.objects.filter(pk=self.id).update(is_active="INACTIVE")    
              #                        instance.save()        
              #                        return "you Need to Renew"              
              #                 return ex_datestr +" Days"






