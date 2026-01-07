from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"hello/index.html")


def sairaj(request):
    return HttpResponse("Hello, Sairaj......")

# ? only taking name from the search bar
#^ def greet(request, namexx):
#^     return HttpResponse(f"hello, {namexx} how are you.......???")


# ? taking a name but giving a response with a separate html page response from the search bar...
def greet(request, name):
    return render(request,"hello/greet.html", {
        "name" : name.capitalize()
    })

