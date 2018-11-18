
from django.shortcuts import render
from django.http import HttpResponse
import helloWorld
import HTMLmaker
import Data_Graph_and_Unzip

def home(request):
    return render(request, 'graph/home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')

def counter(request, num_one='x', num_two='y'):
    f = open("basic-scatter-and-plot.html", "r")
    dingusHTMLString = f.read()
    return HttpResponse(HTMLmaker.splice(dingusHTMLString))
