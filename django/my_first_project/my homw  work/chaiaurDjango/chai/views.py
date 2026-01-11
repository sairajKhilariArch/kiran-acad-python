from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'chai/index.html')

def order(request):
    return render(request, 'chai/order.html')