from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def surat(request):
    return render(request, 'surat.html')

def cluster(request):
    return render(request, 'cluster.html')