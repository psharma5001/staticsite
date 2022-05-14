from django.contrib import admin

from web.models import Page, Website
from .models import *
# Register your models here.
@admin.register(Website)
class websiteAdmin(admin.ModelAdmin):
    list_display =('title','summary','created_on','user','is_generated')

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display =('filename','website')


