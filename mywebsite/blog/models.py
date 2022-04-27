from django.db import models
from django.utils.text import slugify

# Create your models here.

class surat(models.Model):
    no = models.CharField(max_length=50)
    nama = models.TextField(max_length=20)

    def __str__(self):
        return self.nama


class artikel(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField(max_length=1000)
    slug = models.SlugField(editable=False,blank=True,null=True)
    gambar = models.ImageField(upload_to='media/',blank=True,null=True)

    def save(self):
        self.slug=slugify(self.judul)
        super(artikel,self).save()

    def __str__(self):
        return self.judul

class cluster1(models.Model):
    no = models.CharField(max_length=10)
    surat = models.TextField(max_length=1000)
    ayat = models.CharField(max_length=20)
    terjemah = models.TextField(max_length=1000)

    def __str__(self):
        return self.no

class cluster2(models.Model):
    no2 = models.CharField(max_length=10)
    surat2 = models.TextField(max_length=1000)
    ayat2 = models.CharField(max_length=20)
    terjemah2 = models.TextField(max_length=1000)

    def __str__(self):
        return self.no2  

class cluster3(models.Model):
    no3 = models.CharField(max_length=10)
    surat3 = models.TextField(max_length=1000)
    ayat3 = models.CharField(max_length=20)
    terjemah3 = models.TextField(max_length=1000)

    def __str__(self):
        return self.no3    

class cluster4(models.Model):
    no4 = models.CharField(max_length=10)
    surat4 = models.TextField(max_length=1000)
    ayat4 = models.CharField(max_length=20)
    terjemah4 = models.TextField(max_length=1000)

    def __str__(self):
        return self.no4 

class cluster5(models.Model):
    no5 = models.CharField(max_length=10)
    surat5 = models.TextField(max_length=1000)
    ayat5 = models.CharField(max_length=20)
    terjemah5 = models.TextField(max_length=1000)

    def __str__(self):
        return self.no5     

class cluster6(models.Model):
    no6 = models.CharField(max_length=10)
    surat6 = models.TextField(max_length=1000)
    ayat6 = models.CharField(max_length=20)
    terjemah6 = models.TextField(max_length=1000)

    def __str__(self):
        return self.no6   

class cluster7(models.Model):
    no7 = models.CharField(max_length=10)
    surat7 = models.TextField(max_length=1000)
    ayat7 = models.CharField(max_length=20)
    terjemah7 = models.TextField(max_length=1000)

    def __str__(self):
        return self.no7