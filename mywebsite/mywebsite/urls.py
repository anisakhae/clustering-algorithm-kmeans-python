
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
 
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surat/', view.surat, name='surat'),
    path('cluster/', view.cluster, name='cluster'),
    path('blog/',include('blog.urls')),
    path('', view.index, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

