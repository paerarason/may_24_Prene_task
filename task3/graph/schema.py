import graphene
from graphene_django import DjangoObjectType
from .models import Movie

class MovieTYPE(DjangoObjectType):
    class Meta:
        model=Movie
        fields=('id','title','description')

class Query(graphene.ObjectType):
    Movies=graphene.List(MovieTYPE)
    Movies_by_title = graphene.Field(MovieTYPE, title=graphene.String())

    def resolve_Movies(root, info, **kwargs):
        # Querying a list
        return Movie.objects.all()

    def resolve_Movies_by_title(root,info,search=None,**kwargs):
        # Querying a single question
        return Movie.objects.get(title=kwargs["title"])
    
schema = graphene.Schema(query=Query)