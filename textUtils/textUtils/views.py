from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punctuation")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlinerremove(request):
    return HttpResponse("newline remove first")

def spaceremove(request):
    return HttpResponse("spacer remover")

def charcount(request):
    return HttpResponse("charcount")
