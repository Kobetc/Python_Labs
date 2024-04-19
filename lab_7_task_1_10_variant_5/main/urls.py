from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
]
