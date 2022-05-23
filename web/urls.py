from  django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('about/',about, name='about'),
    path('elements/',elements, name='elements'),  
    path('generic/',generic, name='generic'),
    path('sites/user/',my_sites, name='my_sites'),
    path('sites/user/<int:id>/',site_detail, name='site_detail'),

    
]