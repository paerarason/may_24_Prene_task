from rest_framework import serializers
from django.contrib.auth.models import  User
from .models import Blog
class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']


class BlogSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(write_only=True)
    user=UserSeralizer(write_only=True)
    class Meta:
        model=Blog
        fields=['id','title','content','author','user','user_id']
        depth=1
    def validate_author(self,request):
        if Blog.objects.get(author=request.user)!=None:
            return True 
        else:
            return False