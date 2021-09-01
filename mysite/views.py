# I have created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtxt = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepuc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    if removepunc == "on":
        analyzed = ""
        punctuations = ''';:'",<.>/?[{]}!@#$%^&*()_\|`~'''
        for char in djtxt:
            if char not in punctuations:
                analyzed = analyzed + char
        paramet = {'purpose': 'Removed Punctuations',
                   'analyzed_text': analyzed}
        djtxt = analyzed
    if(uppercase == 'on'):
        analyzed = ''
        for char in djtxt:
            analyzed = analyzed + char.upper()
        paramet = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
    if(lineremover == 'on'):
        analyzed = ''
        for char in djtxt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        paramet = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        djtxt = analyzed
    if(spaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtxt):
            if not(djtxt[index] == ' ' and djtxt[index+1] == ' '):
                analyzed = analyzed + char
        paramet = {'purpose': 'removed new lines', 'analyzed_text': analyzed}

    if(removepunc != "on" and lineremover != 'on' and spaceremover != 'on' and uppercase != "on"):
        return HttpResponse("No Functionality selected.")

    return render(request, 'analyze.html', paramet)
