from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Person
from .form import SignINForm,LoginINForm
# Create your views here.
def user_login(request):
  if request.method=="POST":
    print(request.POST["username"],request.POST["password"])
    user_log=authenticate(request,username=request.POST["username"],password=request.POST["password"])
    if user_log !=None:
      return render(request,"dashboard.html",{"user_log":user_log})
    else:
      return HttpResponse(status=403)
  if request.method=="GET": 
    form=LoginINForm()
    return render(request,"login.html",{"form":form})


def user_signin(request): 
  if request.method=="POST":
    form=SignINForm(request.POST)
    if form.is_valid():
       user_obj=User.objects.create_user(username=request.POST["username"],
                                         email=request.POST['email'],
                                         password=request.POST["password"])
       Person.objects.create(user=user_obj)
       form=LoginINForm()
       return redirect("/login")
    else:
       return HttpResponse(status=400)
  if request.method=="GET":
     form=SignINForm()
     return render(request,"signin.html",{"form":form})
