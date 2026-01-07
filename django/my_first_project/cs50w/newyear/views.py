import datetime

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    date = datetime.datetime.now()
    return render(request,"newyear/index.html",{
        "dater" : date.month == 1 and date.day == 1
    })