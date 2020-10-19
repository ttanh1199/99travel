from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')
def discount(request):
    return render(request,'pages/discount.html')
def about(request):
    return render(request,'pages/about.html')