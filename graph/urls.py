from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Graph - Home'),
    path(r'about/', views.about, name='Graph - About'),
    path(r'grapher/', views.grapher),
]
