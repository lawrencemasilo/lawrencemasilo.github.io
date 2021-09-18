from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.views.static import serve 

urlpatterns = [
    path('', views.index, name='index')
]