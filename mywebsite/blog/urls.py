from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path('',views.index,name='index'),
    path('blog/',views.cluster1,name='cluster1'),
    path('blog/blog/',views.cluster2,name='cluster2'),
    path('blog/blog/blog/',views.cluster3,name='cluster3'),
    path('blog/blog/blog/blog',views.cluster4,name='cluster4'),
    path('blog/blog/blog/blog/blog/',views.cluster5,name='cluster5'),
    path('blog/blog/blog/blog/blog/blog/',views.cluster6,name='cluster6'),
    path('blog/blog/blog/blog/blog/blog/blog/',views.cluster7,name='cluster7'),
]
