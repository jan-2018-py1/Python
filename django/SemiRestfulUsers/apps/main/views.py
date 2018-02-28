
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'main/index.html', context)

def new(request):
    return render(request, 'main/new.html')

def edit(request, id):
    context = {
        "get_user": User.objects.get(id=id)
    }
    return render(request, 'main/edit.html', context)

def show(request, id):
    context = {
        "get_user": User.objects.get(id=id)
    }
    return render(request, 'main/show.html', context)

def create(request):
    addUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    user_id = addUser.id
    return HttpResponseRedirect(reverse('show', kwargs={'id':user_id}))

def destroy(req, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('home'))

def update(request):
    user_id = request.POST['id']
    b = User.objects.get(id=user_id)
    b.first_name = request.POST['first_name']
    b.last_name = request.POST['last_name']
    b.email = request.POST['email']
    b.save()
    return HttpResponseRedirect(reverse('show', kwargs={'id':user_id}))