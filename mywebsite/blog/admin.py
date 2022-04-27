from django.contrib import admin
from . import models #titik mengartikan data mengambil dari apps blog

class tampilartikel(admin.ModelAdmin):
    list_display = ['judul']

admin.site.register(models.artikel,tampilartikel)

class tampilcluster1(admin.ModelAdmin):
    list_display = ['no']

admin.site.register(models.cluster1,tampilcluster1)

class tampilcluster2(admin.ModelAdmin):
    list_display = ['no2']

admin.site.register(models.cluster2,tampilcluster2)

class tampilcluster3(admin.ModelAdmin):
    list_display = ['no3']

admin.site.register(models.cluster3,tampilcluster3)

class tampilcluster4(admin.ModelAdmin):
    list_display = ['no4']

admin.site.register(models.cluster4,tampilcluster4)

class tampilcluster5(admin.ModelAdmin):
    list_display = ['no5']

admin.site.register(models.cluster5,tampilcluster5)

class tampilcluster6(admin.ModelAdmin):
    list_display = ['no6']

admin.site.register(models.cluster6,tampilcluster6)

class tampilcluster7(admin.ModelAdmin):
    list_display = ['no7']

admin.site.register(models.cluster7,tampilcluster7)


