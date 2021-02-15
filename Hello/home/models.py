from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,default=None)
    email = models.CharField(max_length=50,default=None)
    phone = models.CharField(max_length=20,default=None)
    start = models.CharField(max_length=20,default=None)
    end = models.CharField(max_length=20,default=None)
    date = models.CharField(max_length=20,default=None)
    desc = models.TextField(default=None)
    #date = models.DateField()
    def __str__(self):
        return self.name
    
class Bus(models.Model):
    Bname = models.CharField(max_length=50,default=None)
    Bemail = models.CharField(max_length=50,default=None)
    Bphone = models.CharField(max_length=20,default=None)
    Bstart = models.CharField(max_length=20,default=None)
    Bend = models.CharField(max_length=20,default=None)
    Bdate = models.CharField(max_length=20,default=None)
    Bticket = models.CharField(max_length=20,default=None)
    Bdesc = models.TextField(default=None)
    #date = models.DateField()
    def __str__(self):
        return self.Bname

class Train(models.Model):
    Tname = models.CharField(max_length=50,default=None)
    Temail = models.CharField(max_length=50,default=None)
    Tphone = models.CharField(max_length=20,default=None)
    Tstart = models.CharField(max_length=20,default=None)
    Tend = models.CharField(max_length=20,default=None)
    Tdate = models.CharField(max_length=20,default=None)
    Tticket = models.CharField(max_length=20)
    Tdesc = models.TextField(default=None)
    #date = models.DateField()
    def __str__(self):
        return self.Tname

class Plain(models.Model):
    Pname = models.CharField(max_length=50,default=None)
    Pemail = models.CharField(max_length=50,default=None)
    Pphone = models.CharField(max_length=20,default=None)
    Pstart = models.CharField(max_length=20,default=None)
    Pend = models.CharField(max_length=20,default=None)
    Pdate = models.CharField(max_length=20,default=None)
    Pticket = models.CharField(max_length=20,default=None)
    Pdesc = models.TextField(default=None)
    #date = models.DateField()
    def __str__(self):
        return self.Pname