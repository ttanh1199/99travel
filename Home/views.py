from django.shortcuts import render
from django.http import HttpResponse
from .models import Review,Discount,Team,About
# Create your views here.
def index(request):
   return render(request, 'pages/home.html',{'Review':Review.objects.all(),'Info':About.objects.all()})
def discount(request):
    return render(request,'pages/discount.html',{'Discount':Discount.objects.all(),'Review':Review.objects.all(),'Info':About.objects.all()})
def about(request):
    return render(request,'pages/about.html',{'Review':Review.objects.all(),'Team':Team.objects.all(),'Info':About.objects.all()})
def contact(request):
    return render(request,'pages/contact.html',{'Info':About.objects.all()})
