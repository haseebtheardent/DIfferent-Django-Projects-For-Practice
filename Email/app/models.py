from django.db import models

# Create your models here.
class Email(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    message = models.TextField()