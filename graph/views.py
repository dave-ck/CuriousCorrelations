
from django.shortcuts import render
from django.http import HttpResponse
import helloWorld
import HTMLmaker
import Data_Graph_and_Unzip

def home(request):
    return HttpResponse(HTMLmaker.splice("<body><p>This is the home page </p></body>"))
        #render(request, 'graph/home.html')

def about(request):
    f = open("about.html", "r")
    htmlboi = f.read()
    return HttpResponse(htmlboi)
        #'<h1>About the bois</h1>')


def grapher(request):
    var1 = request.GET.get("x-variables", "")
    var2 = request.GET.get("y-variables", "")
    print("Var 1:", var1, ", var2:", var2)
    return HttpResponse(HTMLmaker.splice(Data_Graph_and_Unzip.fin_func(var1, var2)))

