from xmlrpc.client import Boolean
from django.db import models
from django.forms import BooleanField
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField(blank= True, null= True)
    price= models.IntegerField(null=True)
    is_active= BooleanField()
    def get_absolute_url(self):
        return reverse("production:product", kwargs={"id":self.id})