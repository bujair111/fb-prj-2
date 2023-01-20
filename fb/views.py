from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'fb-templates/home.html')

def page(request):
    return render (request, 'fb-templates/page.html')

def forget(request):
    return render (request, 'fb-templates/forget.html')   

def craa(request):
    return render (request, 'fb-templates/craa.html')               
