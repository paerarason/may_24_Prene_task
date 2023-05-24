from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    author= models.OneToOneField(User,on_delete=models.CASCADE)