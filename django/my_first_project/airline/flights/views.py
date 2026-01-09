from django.shortcuts import render

from .models import *
# Create your views here.


def index(request):
    return render(request,"flights/index.html",{
        "flights":Flights.objects.all()
    })
    
    
def flight(request,flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all()
    })
    
    
def book(request,flight_id):
    if request.method == "POST":
        flight = Flights.object.get(pk = flight_id)
    return render(request,"flight/book.html",{
        
    })