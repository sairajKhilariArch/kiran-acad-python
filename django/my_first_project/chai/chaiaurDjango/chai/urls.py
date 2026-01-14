
from django.urls import include,path
from . import views

urlpatterns = [
    path("",views.index, name="HOME"),
    path("order/",views.order, name="ORDER"),
    path("all_chai/",views.all_chai,name="ALL_CHAI"),
    path("<int:chai_id>",views.chai_detail,name="CHAI_DETAIL"),
    
    path("chai_store/" , views.chai_stores , name="CHAI_STORE")
]
