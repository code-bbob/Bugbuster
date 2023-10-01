from django.shortcuts import render, HttpResponse, redirect 
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post



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
    allPosts = Post.objects.all()  
    context = {'allPosts': allPosts}
    messages.success(request, 'Posted Sucessfully')
    return render(request, 'home/home.html', context)
    

def blogpersonal(request, slug):
    return HttpResponse('')

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

def company(request):
    return render(request, 'home/company.html')



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
    

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def post(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        title = request.POST.get('title')
        post = Post(author=author, content=content,title=title, date=datetime.today())
        post.save()
        messages.success(request, 'Blog post successfully')

    return render(request, 'home/post.html')
