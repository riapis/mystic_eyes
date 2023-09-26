from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    element = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    power = models.PositiveIntegerField()
    description = models.TextField()