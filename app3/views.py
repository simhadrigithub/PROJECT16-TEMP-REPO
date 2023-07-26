from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def fifth(request):
    return render(request,'fifth.html')

def sixth(request):
    return render(request,'sixth.html')

def nature(request):
    return HttpResponse("<h1>good behaviour nature persons</h1>")
