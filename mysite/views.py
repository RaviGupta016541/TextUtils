#i have created this file - ravi
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param={'Name':'Ravi','Place':'Jhansi','Number':'77689'}
    return render(request,'index2.html',param)
def links(request):
    return render(request,'links.html')
def analyze(request):
    dtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunch','off')
    Fullcaps=request.POST.get('Fullcaps','off')
    NewLine=request.POST.get('NewLine','off')
    Space=request.POST.get('Space','off')
    punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    s=''
    pur=""
    if removepunc =='on':
       for i in dtext:
           if i not in punc:
               s+=i
       pur=pur+" and "+"Remove punc"

    if Fullcaps=='on':
        s=s.upper()
        pur = pur + " and " + "Full capatalize"

    if NewLine=='on':
        dtext=s
        s=''
        for i in dtext:
            if i !='\n' and i!='\r':
                s += i
        pur = pur + " and " + "Remove NewLine"

    if Space=='on':
        dtext = s
        s = ''
        for index,char in enumerate(dtext):
                if not(dtext[index]==' ' and dtext[index+1]==' '):
                    s=s+char
        pur = pur + " and " + "Remove ExtraSpace"
    if (removepunc != "on" and NewLine != "on" and Space != "on" and Fullcaps != "on"):
        return HttpResponse("please select any operation and try again")
    par = {'analyzed_text': s, 'purpose': pur[4:]}
    return render(request, 'analyze.html', par)

