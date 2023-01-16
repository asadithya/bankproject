from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class District(models.Model):
    dname=models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.dname
class Branch(models.Model):
    bname=models.CharField(max_length=250,unique=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.bname

class Applicationform(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day   = models.CharField(max_length=100)
    year    = models.CharField(max_length=100)
    gender  = models.CharField(max_length=100)
    age     = models.CharField(max_length=100)
    phone   = models.CharField(max_length=100)
    email   = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    materials_provide = models.TextField()
    Branch_id = models.ForeignKey(Branch , on_delete=models.CASCADE)
    District_id = models.ForeignKey(District , on_delete=models.CASCADE)



