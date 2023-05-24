from .models import Blog
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes

@api_view(["GET","DELETE"])
@permission_classes([IsAuthenticated])
def Blog_view(request,pk):
    try:
       blog=Blog.objects.filter(id=pk,author=request.user)
    except Blog.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
       blog_obj=BlogSerializer(blog)
       return Response(blog_obj.data,status=status.HTTP_200_OK)       
    else:
       blog.delete()
       return Response(status=status.HTTP_200_OK)

@api_view(["GET","POST","PATCH"])
@permission_classes([IsAuthenticated])
def Blog_Patch_post(request):
    if request.method=="POST":
       blog_obj=BlogSerializer(request,data=request.data)
       if blog_obj.is_valid():
         return Response(blog_obj.data,status=status.HTTP_200_OK) 
       else:
          return Response(status=status.HTTP_400_BAD_REQUEST)   
    elif request.method=="GET":
       blog=Blog.objects.filter(auther=request.user)
       blog_obj=BlogSerializer(blog,many=True)
       return Response(blog_obj.data,status=status.HTTP_200_OK) 
    else:
       blog_obj=BlogSerializer(request,data=request.data,partial=True)
       if blog_obj.validate_author(request):
          return Response(blog_obj.data,status=status.HTTP_200_OK)
       else:
           return Response(status=status.HTTP_403_FORBIDDEN)