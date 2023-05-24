from django.urls import path
from .views import Blog_Patch_post,Blog_view
urlpatterns=[
             path("blog/<int:pf>/",Blog_view),
             path("blog/",Blog_Patch_post),
]