from django.shortcuts import render
from . import models

def index(request):
    data_artikel = models.artikel.objects.all()
    context = {
        'halaman' :'Data hasil Cluster',
        'data' :data_artikel,
    }
    print(data_artikel)
    return render(request, 'blog/index.html',context)

def cluster1(request):
    data_cluster1 = models.cluster1.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster1,
    }
    print(data_cluster1)
    return render(request, 'blog/cluster1.html', context)

def cluster2(request):
    data_cluster2 = models.cluster2.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster2,
    }
    print(data_cluster2)
    return render(request, 'blog/cluster2.html', context)

def cluster3(request):
    data_cluster3 = models.cluster3.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster3,
    }
    print(data_cluster3)
    return render(request, 'blog/cluster3.html', context)

def cluster4(request):
    data_cluster4 = models.cluster4.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster4,
    }
    print(data_cluster4)
    return render(request, 'blog/cluster4.html', context)

def cluster5(request):
    data_cluster5 = models.cluster5.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster5,
    }
    print(data_cluster5)
    return render(request, 'blog/cluster5.html', context)

def cluster6(request):
    data_cluster6 = models.cluster6.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster6,
    }
    print(data_cluster6)
    return render(request, 'blog/cluster6.html', context)

def cluster7(request):
    data_cluster7 = models.cluster7.objects.all()
    context = {
        'halaman' : 'Detail cluster',
        'data' : data_cluster7,
    }
    print(data_cluster7)
    return render(request, 'blog/cluster7.html', context)