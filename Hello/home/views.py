from django.shortcuts import render,HttpResponse
# from datetime import datetime
from .models import *
from .models import Bus
from django.contrib import messages
import socket

# Create your views here.
def index(request):
    
    return render(request, 'index.html',)
    
def carrental(request):
    return render(request, 'carrental.html',)

def services(request):
    return render(request, 'services.html',)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        start = request.POST.get('start')
        end = request.POST.get('end')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, start=start, end=end, date=date,desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def train(request):
    if request.method == "POST":
        Tname = request.POST.get('Tname')
        Temail = request.POST.get('Temail')
        Tphone = request.POST.get('Tphone')
        Tstart = request.POST.get('Tstart')
        Tend = request.POST.get('Tend')
        Tdate = request.POST.get('Tdate')
        Tticket = request.POST.get('Tticket')              
        Tdesc = request.POST.get('Tdesc')
        train = Train(Tname=Tname, Temail=Temail, Tphone=Tphone, Tstart=Tstart, Tend=Tend, Tdate=Tdate, Tticket=Tticket, Tdesc=Tdesc)
        train.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'train.html',)

def bus(request):
    if request.method == "POST":
        Bname = request.POST.get('Bname')
        Bemail = request.POST.get('Bemail')
        Bphone = request.POST.get('Bphone')
        Bstart = request.POST.get('Bstart')
        Bend = request.POST.get('Bend')
        Bdate = request.POST.get('Bdate')
        Bticket = request.POST.get('Bticket')      
        Bdesc = request.POST.get('Bdesc')
        bus = Bus(Bname=Bname, Bemail=Bemail, Bphone=Bphone, Bstart=Bstart, Bend=Bend, Bdate=Bdate, Bticket=Bticket, Bdesc=Bdesc)
        bus.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'bus.html',)

def plain(request):
    if request.method == "POST":
        Pname = request.POST.get('Pname')
        Pemail = request.POST.get('Pemail')
        Pphone = request.POST.get('Pphone')
        Pstart = request.POST.get('Pstart')
        Pend = request.POST.get('Pend')
        Pdate = request.POST.get('Pdate')
        Pticket = request.POST.get('Pticket')      
        Pdesc = request.POST.get('Pdesc')
        plain = Plain(Pname=Pname, Pemail=Pemail,Pphone=Pphone, Pstart=Pstart, Pend=Pend, Pdate=Pdate, Pticket=Pticket, Pdesc=Pdesc)
        plain.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'plain.html',)

def carform(request):
    return render(request, 'carform.html',)


    