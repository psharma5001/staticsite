import re
from bs4 import PageElement
from django.shortcuts import render
from multiprocessing import AuthenticationError
from .models import Website,Page
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import *

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    ctx = {}
    ctx['title'] = "Home"
    return render(request,'index.html',ctx)


def about(request):
    ctx = {}
    return render(request,'about.html')

def elements(request):
    ctx = {}
    ctx['title'] = "Element"
    return render(request,'elements.html')
    
    
def generic(request):
    ctx = {}
    ctx['title'] = "Generic"
    return render(request,'generic.html')

@login_required
def my_sites(request):
    ctx = {}
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST, request.user)
        if form.is_valid():
            website = form.save(commit=False)
            website.user = request.user
            website.save()
            messages.success(request, "Blank static site generated, Now add pages to site")
            return redirect('my_sites')
    ctx['form'] = form
    websites = Website.objects.filter(user=request.user).all()
    ctx['title'] = "My Sites"
    ctx['websites'] = websites
    return render(request,'mysites.html',ctx)

@login_required
def site_detail(request,id):
    ctx = {}
    ctx = {}
    form = PageForm()
    web = Website.objects.get(id=id)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.website = web
            page.save()
            messages.success(request, "Page generated, Edit pages to ")
            return redirect('my_sites')
    ctx['form'] = form
    ctx['website'] = web
    ctx['pages'] = Page.objects.filter(website=id).all()
    ctx['title'] = web.title
    return render(request,'site_detail.html',ctx)

@login_required
def generate_static_sitet(request,id):
    website = Website.objects.get(id=id)
    ctx = {}
    ctx['title'] = "Generated"
    ctx['website'] = website
    return render(request,'results.html',ctx)
