from django.shortcuts import render, HttpResponse, redirect 
from datetime import datetime
from django.contrib import messages
from blog.models import Post


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,'blog/blogHome.html')

def blogPost(request, slug):
    return HttpResponse(f'This is blog post: {slug}')
    
def kawadi(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        post = Post(author=author, content=content, date=datetime.today())
        post.save()
        messages.success(request, 'Blog post successfully')

    return render(request, 'blog/kawadi.html')
