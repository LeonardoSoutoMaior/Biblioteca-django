from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('kkk')

def cadastro(request):
    return render(request, 'cadastro.html')