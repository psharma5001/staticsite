from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from flask import flash
from .forms import *
from .utils import *
import re
from .models import Website,Page

# Create your views here.
def index(request):
    ctx = {}
    web = Website.objects.order_by('-created_on').all() 
    ctx['title'] = "Home"
    ctx['websites'] = web
    ctx['summary'] = "static site generator is a free, open-source, and easy-to-use static site generator for Django."
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
    form = PageForm()
    web = Website.objects.get(id=id)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.website = web
            page.save()
            messages.success(request, "Page generated, Edit pages to ")
            return redirect('site_detail',id=id)
    ctx['form'] = form
    ctx['website'] = web
    ctx['pages'] = Page.objects.filter(website=id).all()
    ctx['title'] = web.title
    ctx['summary'] = web.summary
    request.session['site_id'] = id
    return render(request,'site_detail.html',ctx)

@login_required
def site_download(request,id):
    ctx = {}
    web = Website.objects.get(id=id)
    ctx['website'] = web

    if request.method == 'POST':
        pages = []
        files = request.POST.getlist('files')
        for file in files:
            page = Page.objects.get(filename=file)
            code = generate_html_from_md(page.text)
            saved_file = create_html_file(page.filename,code)
            pages.append(saved_file)

        zip_file = create_zip("_".join(web.title.split()),pages)
        response = FileResponse(open(zip_file,'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(zip_file)
        messages.success(request, f'{zip_file} was downloaded')
        return response

    ctx['title'] = web.title + " - Download ⬇️"
    ctx['summary'] = 'Download ' + web.title + ' as a static site'
    ctx['pages'] = Page.objects.filter(website=id).all()
    return render(request,'site_download.html',ctx)

@login_required
def site_delete(request,id):
    web = Website.objects.get(id=id)
    web.delete()
    messages.success(request, "Site deleted")
    return redirect('my_sites')

@login_required
def page_edit(request,id):
    ctx = {}
    page = Page.objects.get(id=id)
    form = PageForm(instance=page)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()
            messages.success(request, "Page updated")
            return redirect('site_detail',id=page.website.id)
    ctx['form'] = form
    ctx['page'] = page
    ctx['title'] = page.website.title

    return render(request,'page_edit.html',ctx)

@login_required
def page_delete(request,id):
    ctx = {}
    page = Page.objects.get(id=id)
    page.delete()
    messages.success(request, "Page deleted")
    return redirect('site_detail',id=page.website.id)

@login_required
def page_preview(request,id):
    ctx = {}
    page = Page.objects.get(id=id)
    ctx['page'] = page
    ctx['title'] = page.website.title
    code = generate_html_from_md(page.text)
    print(code)
    ctx['code'] = code
    return render(request,'page_preview.html',ctx)

@login_required
def generate_static_site(request,id):
    website = Website.objects.get(id=id)
    ctx = {}
    ctx['title'] = "Generated"
    ctx['website'] = website
    return render(request,'results.html',ctx)
