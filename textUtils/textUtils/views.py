from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Home")
    params = {"name":"Akash",
              "city":"Delhi"}
    return render(request,"index.html",params)

def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punctuation")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlinerremove(request):
    return HttpResponse("newline remove first")

def spaceremove(request):
    return HttpResponse("spacer remover")

def charcount(request):
    return HttpResponse("charcount")
