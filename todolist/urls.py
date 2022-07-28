from django.urls import path
from todolist import views


app_name = "todolist" # app name
urlpatterns=[
    path("",views.index,name="index")
]

#def index(request):
    #return render(request,"todolist/index.html")
