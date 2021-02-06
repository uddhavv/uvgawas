from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,default=None)
    email = models.CharField(max_length=50,default=None)
    phone = models.CharField(max_length=20,default=None)
    start = models.CharField(max_length=20,default=None)
    end = models.CharField(max_length=20,default=None)
    date = models.CharField(max_length=20,default=None)
    mode = models.CharField(max_length=20,default=None)
    desc = models.TextField(default=None)
    #date = models.DateField()
    def __str__(self):
        return self.name
    
