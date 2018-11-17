from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Graph - Home'),
    path('about/', views.about, name='Graph - About'),
    path('counter/first=<int:num_one>&second=<int:num_two>/', views.counter, name='Graph - counter'),
]
