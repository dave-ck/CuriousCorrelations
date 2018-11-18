
from django.shortcuts import render
from django.http import HttpResponse
import helloWorld

def home(request):
    return render(request, 'graph/home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')

def counter(request, num_one='x', num_two='y'):
    return HttpResponse('<h1>The product of the two numbers is {} </h1>'.format(helloWorld.prod(num_one, num_two)))
