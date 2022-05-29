from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name ="authen"
urlpatterns = [
    path('signin/', login_view, name="login"),
    path('signup/', register_user, name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    
    
]