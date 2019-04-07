from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context['hello'] = {'hello world!','h1','h2'}
    return render( request , 'index.html' , context )