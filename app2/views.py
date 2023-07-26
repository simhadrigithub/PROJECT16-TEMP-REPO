from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def third(request):
    return render(request,'third.html')

def fourth(request):
    return render(request,'fourth.html')

def nature(request):
    return HttpResponse("<h1>good behaviour nature persons</h1>")
