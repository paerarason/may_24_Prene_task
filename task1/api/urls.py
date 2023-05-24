from django.urls import path
from .views import user_method,usersmethod
urlpatterns=[
    path('users/',usersmethod),
    path('users/<int:pk>',user_method)
]