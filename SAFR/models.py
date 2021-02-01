from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    company_name = models.CharField(max_length=190,null=True)
    phone = models.CharField(max_length=190,null=True)
    address= models.CharField(max_length=190,null=True)
    

# detels of visa 
class Visa(models.Model):
    name=models.CharField(max_length=190,null=True)
    pric_visa=models.CharField(max_length=200,null=True)
    Your_documents=models.CharField(max_length=300,null=True)
    Duration_release=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

    
    

# detels of trip by ADmin 
class Bookflight(models.Model):

    from_city=models.CharField(max_length=190,null=True)
    To_city=models.CharField(max_length=190,null=True)
    seat_type=models.CharField(max_length=190,null=True)
    pric=models.CharField(max_length=190,null=True)
    seat_nuper=models.CharField(max_length=190,null=True)
    Airline_type=models.CharField(max_length=200,null=True)
    Airline_nump=models.CharField(max_length=200,null=True)
    Data_trib=models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.from_city

    


   
# model trip by coustemer
class Ordertrip(models.Model):
    from_city=models.CharField(max_length=190,null=True)
    To_city=models.CharField(max_length=190,null=True)
    seat_type=models.CharField(max_length=190,null=True)
    seat_nuper=models.CharField(max_length=190,null=True)
    number_infants=models.CharField(max_length=20,null=True)
    Number_adults=models.CharField(max_length=190,null=True)
    number_children=models.CharField(max_length=190,null=True)
    Data_go=models.CharField(max_length=190,null=True)
    Data_back=models.CharField(max_length=190,null=True)
    Airline_type=models.CharField(max_length=200,null=True)
    Trip_type=models.CharField(max_length=200,null=True)
    data_creat=models.DateField(auto_now_add=True,null=True)
    phone = models.CharField(max_length=190,null=True)
    full_name = models.CharField(max_length=190,null=True)
      

  





