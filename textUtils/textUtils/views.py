from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Home")
    params = {"name":"Akash",
              "city":"Delhi"}
    return render(request,"index.html",params)

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newLineRemove = request.GET.get('newLineRemove','off')
    extraSpaceRemove = request.GET.get('extraSpaceRemove','off')
    charcount = request.GET.get('charcount','off') 

    print(removepunc)
    print(djtext)
    params=""
    newText = ''
    punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
        for c in djtext:
         if c not in punctuations:
            newText+=c
        params = {'purpose':'Remove Punctuation','analyzed_text':newText}         
    elif fullcaps =="on":
       newText= str.upper(djtext)
       params = {'purpose':'Changed to Uppercase','analyzed_text':newText}
    elif newLineRemove=="on":
       for c in djtext:
           if c=="\n":
              newText+=djtext
              break
       params = {'purpose':'NewLineRemoved','analyzed_text':newText}       
    elif extraSpaceRemove=="on":
       for i,c in enumerate(djtext):
          if not(djtext[i]==" " and djtext[i+1]==" "):
             newText+=c
       params = {'purpose':'ExtraSpaceRemoved','analyzed_text':newText}             
    elif charcount=="on":
       count = str(len(djtext.replace(" ","")))

       newText = "No of Characters is:"+count
       params ={'purpose':'CharCount','analyzed_text':newText}    
    else:
        newText=djtext
           
    # return HttpResponse("remove punctuation")
    return render(request,'analyze.html',params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlinerremove(request):
#     return HttpResponse("newline remove first")

# def spaceremove(request):
#     return HttpResponse("spacer remover")

# def charcount(request):
#     return HttpResponse("charcount")
