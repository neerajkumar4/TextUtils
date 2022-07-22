# I have created this file - Neeraj
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext=request.POST.get('text', 'default')

    punrem=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlinerem=request.POST.get('newlineremover', 'off')
    extraspacerem= request.POST.get('extraspaceremover', 'off')
    punc_list = '''./<>?;:""''{}[]()!@#$%^&*-_`~|\,'''

    if punrem=="on":
        analyzed = ""
        for char in djtext:
            if char not in punc_list:
                analyzed=analyzed+char
        djtext=analyzed
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed= analyzed + char.upper()
        djtext = analyzed

    if newlinerem=='on':
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!="\r":
                analyzed = analyzed +char
        djtext = analyzed
    if extraspacerem=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index-1]==" " and djtext[index]==" ":
                pass
            else:
                analyzed = analyzed +char
        djtext = analyzed
    if punrem!="on" and fullcaps!="on" and newlinerem!="on" and extraspacerem!="on":
        return render(request, 'Error.html')
    params = {'purpose': 'performed operations', 'analyzed_text': djtext}
    return render(request, 'analize.html', params)
