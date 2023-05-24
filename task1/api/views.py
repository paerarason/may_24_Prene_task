from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from .models import User
from .seralizer import UserSerializer
# Create your views here.
@api_view(["GET","POST"])
def usersmethod(request):
    if request.method=="GET":
        user=User.objects.all()
        user=UserSerializer(user,many=True)
        return Response(user.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
       user=UserSerializer(data=request.data)
       if user.is_valid():     
            user.save()
            return Response(user.data,status=status.HTTP_201_CREATED)
       else:
          return HttpResponse(status=400)  
       
@api_view(["GET","DELETE"])
def user_method(request,pk):
   if request.method=="GET":
       try:
           user=User.objects.get(id=pk)
           user=UserSerializer(user)
           return Response(user.data,status=status.HTTP_200_OK)
       except:
           return HttpResponse(status=404)  
   else:
       user=User.objects.get(id=pk)
       user.delete()
       return Response(status=status.HTTP_200_OK)
   