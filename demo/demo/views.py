from django.http import render,HttpResponse
#return a text file

#def txt(request):
#    return HttpResponse(request,file.txt)
 
def index(request):
    return HttpResponse("hello Sir")

def about(request):
    return HttpResponse("About Sir")