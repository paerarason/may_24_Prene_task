from django.db import models

# Create your models here.
'''Implement a GraphQL API using any Python framework of your choice that allows 
    users to query and retrieve information about movies. 
    The API should support queries such as retrieving a list of movies,
    searching for movies by title, and retrieving movie details.         '''

class Movie(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()