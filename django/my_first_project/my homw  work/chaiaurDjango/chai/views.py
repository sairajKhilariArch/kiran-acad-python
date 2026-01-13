from django.shortcuts import render,get_list_or_404,get_object_or_404
from . import models


# Create your views here.

def index(request):
    return render(request, 'chai/index.html')

def order(request):
    return render(request, 'chai/order.html')



def all_chai(request):
    chais = models.ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{
        'chais':chais
    })
    
def chai_detail(request,chai_id):
    chai = get_object_or_404(models.ChaiVarity ,pk=chai_id)
    return render(request,'chai/chai_detail.html',{
        'chai': chai
    })

