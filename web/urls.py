from  django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('login',login, name='login'),
    path('signup',signup, name='signup'),
    path('about/',about, name='about'),
    path('elements/',elements, name='elements'), 
     path('generic/',generic, name='generic'),
    
]