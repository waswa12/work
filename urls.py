from importlib.resources import path
from library import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('details.html', views.detail, name='details'),
]