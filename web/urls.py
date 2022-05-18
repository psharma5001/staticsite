from  django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('signup/', register_user, name="register"),
    path('signin/', login_view, name="login"),
]