from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index_home, name='index'),
    path('keyword', views.keyword, name='keyword'),
    path('timeline', views.timeline, name='timeline'),
]