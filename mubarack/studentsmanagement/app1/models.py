from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__ (self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=20)
    department = models.ForeignKey(catogory, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    

