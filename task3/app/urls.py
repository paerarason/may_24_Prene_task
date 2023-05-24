from django.urls import path
from .views import user_login,user_signin
urlpatterns=[
    path("login/",user_login),
    path("signin/",user_signin),
]