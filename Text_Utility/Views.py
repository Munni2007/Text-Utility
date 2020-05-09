#I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index2.html')

def analyze(request):
    #get text
    djtext=request.POST.get('text', 'default')
    
    #get checkbox value
    removepunc=request.POST.get('removepunc', 'default')
    upcase=request.POST.get('UPERCASE','default')
    nlr=request.POST.get('new_line_remover','default')
    sr=request.POST.get('space_remover','default')

    # to check wich checkbox is on
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
        #for passing values in templates         
        ls={'purpose':'remove punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        
    if(upcase=='on'):
        analyzed=""
        analyzed=djtext.upper()
        ls={'purpose':'upercase','analyzed_text':analyzed}
        djtext=analyzed

    if(nlr=='on'):
        analyzed=""
        for i in djtext:
            if i !='\n' and i !='\r':
                analyzed=analyzed+i;
        ls={'purpose':'new line remove','analyzed_text':analyzed}
        djtext=analyzed
        
    if(sr=='on'):
        analyzed=""
        for i,c in enumerate(djtext):
            if djtext[i]==' ' and djtext[i+1]==' ':
                pass
            else:
                analyzed=analyzed+c;
        ls={'purpose':'extra space remove','analyzed_text':analyzed}
        djtext=analyzed

    if removepunc!='on' and upcase!='on' and nlr!='on' and sr!='on':
        return HttpResponse("Please select any operation and try again!!")

    return render(request, 'analyzed.html', ls)
    
    



