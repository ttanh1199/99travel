from django.urls import path
from . import views

urlpatterns = [
   path('home', views.index),
   path('discount', views.discount),
   path('about', views.about),
   path('contact',views.contact)
]