from django.shortcuts import render, HttpResponse, redirect 
from home.models import Contact,Post
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def loginuser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            return redirect('/login')
        
    if request.method == 'GET':
        return render(request, 'home/index.html')

def signup(request):
    return render(request, 'home/signup.html')

@login_required(login_url='/login')
def home(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        posts = Post(author=author, content=content, date=datetime.today())
        posts.save()
        messages.success(request, 'Posted Sucessfully')
        return render(request, 'home/home.html')
    
    else:
        return render(request, 'home/home.html')

def link(request):
    return HttpResponse('This is a link')

def action(request):
    return HttpResponse('This is an action')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Messages sent successfully')
    
    return render(request, 'home/contact.html')

def logoutUser(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password')
        if password == password1:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('Doneeeeeeeeeeeeeeeeee')
            return redirect('/')
        else:
            return redirect('/signup')
    else:
        return render(request, 'home/signup.html')
