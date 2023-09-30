from django.shortcuts import render, HttpResponse, redirect 
from datetime import datetime
from django.contrib import messages
from blog.models import Post


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/blogHome.html',  context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)
    
def post(request):
    
    
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        title = request.POST.get('title')
        post = Post(author=author, content=content, date=datetime.today())
        post.save()
        messages.success(request, 'Blog post successfully')

    return render(request, 'blog/post.html')
