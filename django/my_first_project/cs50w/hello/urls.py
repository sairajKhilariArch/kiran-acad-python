from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index page hello"),
    
    path("sairajss", views.sairaj, name= "sairajs"),
    
    # ? only taking name from the search bar
    # ^ path("<str:namexx>",views.greet,name = "greet's the entered name"),

    path("<str:name>", views.greet, name = "greets the entered name by html page"),
    
    
    
]
