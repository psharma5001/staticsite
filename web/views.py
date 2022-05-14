from django.shortcuts import render
from web.models import Website

# Create your views here.
def index(request):
    ctx = {}
    return render(request,'index.html',ctx)
