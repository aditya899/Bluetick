from django.db import models
from django.db.models.deletion import CASCADE

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True,auto_created=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)

class Remarks(models.Model):
    remark_id = models.IntegerField(primary_key=True)
    address_id = models.ForeignKey(Address,on_delete=models.CASCADE)
