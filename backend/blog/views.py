from django.shortcuts import render, HttpResponse, redirect 


def blogHome(request):
    return HttpResponse('This is blog home')

def blogPost(request, slug):
    return HttpResponse(f'This is blog post: {slug}')
    