from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.

posts = [
        {'id':1,'title':'Post 1','content':'Content of the Post 1'},
        {'id':2,'title':'Post 2','content':'Content of the Post 2'},
        {'id':3,'title':'Post 3','content':'Content of the Post 3'},
        {'id':4,'title':'Post 4','content':'Content of the Post 4'},
        {'id':5,'title':'Post 5','content':'Content of the Post 5'},
        {'id':6,'title':'Post 6','content':'Content of the Post 6'}
    ]

def index(request):
    blogs_title = 'Latest Posts'
    return render(request,'index.html',{'blogs_title':blogs_title,'posts':posts})

def detail(request,post_id):
    post = next((item for item in posts if item['id'] == post_id ),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post value is {post}')
    return render(request,'detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the redirected new url")