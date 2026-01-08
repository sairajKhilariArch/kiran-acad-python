from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    # email = forms.EmailField(label = "Email")
    # age = forms.IntegerField(label = "AGE" , min_value = 0, max_value = 100)
    # ssa = forms.URLField(label = "URL")









# Create your views here.
# tasks = []


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"tasks/index.html", {
        "tasks101" : request.session["tasks"]
    })
    
    

def add_tasks(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid() : 
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("Tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form" : form
            })
            
    return render(request,"tasks/add.html",{
        "form" : NewTaskForm()
    })

