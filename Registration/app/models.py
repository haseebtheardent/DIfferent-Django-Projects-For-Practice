from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()
    message = models.TextField()
    def __str__(self):
       return 'Message From' + ' ' + self.name + ' ' + self.email