from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class catogory(models.Model):
    name = models.CharField(max_length=20)

    def __str__ (self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=20)
    catogory = models.ForeignKey(catogory, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos')
    price = models.IntegerField()

class cartu(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    contity = models.PositiveIntegerField(default=0)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    
