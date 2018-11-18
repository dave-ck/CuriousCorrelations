
from django.shortcuts import render
from django.http import HttpResponse
import helloWorld
import HTMLmaker
import Data_Graph_and_Unzip

def home(request):
    return render(request, 'graph/home.html')

def about(request):
    f = open("about.html", "r")
    htmlboi = f.read()
    return HttpResponse(htmlboi)
        #'<h1>About the bois</h1>')

def grapher(request):
    var1 = request.GET.get("first", "")
    var2 = request.GET.get("second", "")
    print("Var 1:", var1, ", var2:", var2)
    f = open("basic-scatter-plot.html", "r")
    dingusHTMLString = f.read()
    return HttpResponse(HTMLmaker.splice(Data_Graph_and_Unzip.fin_func(var1, var2)))

