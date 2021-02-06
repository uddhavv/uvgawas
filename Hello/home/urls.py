from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('carrental',views.carrental,name='carrental'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact1'),
    path('train',views.Train,name='Train'),
    path('bus',views.Bus,name='Bus'),
    path('plain',views.Plain,name='Plain'),

]
