from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    element = models.CharField(max_length=255)
    amount = models.IntegerField()
    power = models.IntegerField()
    description = models.TextField()