from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,"shop/index.html",{'product':products})

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")

def productView(request):
    return HttpResponse("productView")

def checkout(request):
    return HttpResponse("checkout")