
from django.urls import include,path
from . import views

urlpatterns = [
    path("",views.index, name="HOME"),
    path("order/",views.order, name="ORDER"),
    
]
