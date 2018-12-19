from django.shortcuts import render
from django.http import HttpResponse
import helloWorld
import HTMLmaker
import graph_maker


def home(request):
    return HttpResponse(HTMLmaker.splice("<body><p></p></body>"))
    # render(request, 'graph/home.html')


def about(request):
    f = open("aboutpage.html", "r")
    print("about page loaded")
    htmlboi = f.read()
    return HttpResponse(htmlboi)


def grapher(request):
    var1 = request.GET.get("x-variables", "")
    var2 = request.GET.get("y-variables", "")
    print("Var 1:", var1, ", var2:", var2)
    return HttpResponse(HTMLmaker.splice(graph_maker.graph(var1, var2)))
