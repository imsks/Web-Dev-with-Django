from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    return HttpResponse("Hi a")

