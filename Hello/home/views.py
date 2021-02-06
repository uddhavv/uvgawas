from django.shortcuts import render,HttpResponse
# from datetime import datetime
from .models import Contact
from django.contrib import messages

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
        mode= request.POST.get('mode')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, start=start, end=end, date=date, mode=mode, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def Train(request):
    return render(request, 'train.html',)

def Bus(request):
    return render(request, 'bus.html',)

def Plain(request):
    return render(request, 'plain.html',)
