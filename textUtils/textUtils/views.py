from django.http import HttpResponse
from django.shortcuts import render
import re
def about(request):
    params = {"name":"Akash", 
              "city":"Delhi"}
    return render(request,"about.html",params)

def index2(request):
    return render(request,"index2.html")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newLineRemove = request.POST.get('newLineRemove','off')
    extraSpaceRemove = request.POST.get('extraSpaceRemove','off')
    charcount = request.POST.get('charcount','off') 

    print(removepunc)
    print(djtext)
    params=""
    newText = ''
    punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
      #   if(removepunc=="on" and fullcaps=="on"):
      #     newText = re.sub("[^a-zA-Z0-9]","",djtext) 
      #     params={'purpose':'Remove Punctuation and fullcaps','analyzed_text':newText.upper()}  
      #   else:   
         for c in djtext:
          if c not in punctuations:
            newText+=c
          params = {'purpose':'Remove Punctuation','analyzed_text':newText}   
         djtext=newText       
    if fullcaps =="on":
       newText= str.upper(djtext)
       params = {'purpose':'Changed to Uppercase','analyzed_text':newText}
       djtext=newText
    if newLineRemove=="on":
       newText = re.sub('[\n\r]',"",djtext)
       params = {'purpose':'NewLineRemoved','analyzed_text':newText}   
       djtext=newText    
    if extraSpaceRemove=="on":
       newText = re.sub('\s+'," ",djtext)
             
       params = {'purpose':'ExtraSpaceRemoved','analyzed_text':newText}  
       djtext=newText           
    if charcount=="on":
       count = str(len(djtext.replace(" ","")))

       newText = "No of Characters is:"+count+"\nNewText:"+djtext.replace(" ","")
       params ={'purpose':'CharCount','analyzed_text':newText}    
     
    if (removepunc!="on" and fullcaps !="on" and newLineRemove!="on" 
       and extraSpaceRemove!="on" and charcount!="on" and charcount!="on"):
       return HttpResponse("error Bitch")
           
    return render(request,'analyze.html',params)


