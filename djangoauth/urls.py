from django.urls import re_path
from . import views
urlpatterns = [
 re_path('login', views.login),
 re_path('signup', views.sign_Up),
 re_path('test_token', views.test_token),
]
