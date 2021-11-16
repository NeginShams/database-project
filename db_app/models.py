from django.db import models

class MyUser(models.Model):
    name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.TextField()
    #gender = models.BooleanField()


