from  django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('about/',about, name='about'),
    path('elements/',elements, name='elements'),  
    path('generic/',generic, name='generic'),
    path('sites/user/',my_sites, name='my_sites'),
    path('sites/user/<int:id>/',site_detail, name='site_detail'),
    path('sites/download/<int:id>/',site_download, name='site_download'),
    
    path('sites/user/<int:id>/delete/',site_delete, name='site_delete'),
    path('page/edit/<int:id>/',page_edit, name='page_edit'),
    path('page/delete/<int:id>/',page_delete, name='page_delete'),
    path('page/preview/<int:id>/',page_preview, name='page_preview'),
    # download link
    
    
]