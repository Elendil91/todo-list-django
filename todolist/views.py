from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect #added
from django import forms 
from django.urls import reverse 
# Create your views here.



task = []

#def index(request):
    #return HttpResponse("Hello World!")

def index(request):
    if request.method == "POST":
        form = NewTextForm(request.POST)
            
        if form.is_valid():
            tasks = form.cleaned_data["tasks"]
            task.append(tasks)
        return HttpResponseRedirect(reverse("todolist:index"))
        
    return render(request,"todolist/index.html",{
        "tasks":task, # your List name 
        "form":NewTextForm(),
    })

class NewTextForm(forms.Form):
    tasks = forms.CharField(label="New Task:")  # new text input

