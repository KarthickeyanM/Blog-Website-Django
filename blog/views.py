from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
import logging
from .models import Post, AboutUs
from .forms import ContactForm
# Create your views here.

# posts = [
#         {'id':1,'title':'Post 1','content':'Content of the Post 1'},
#         {'id':2,'title':'Post 2','content':'Content of the Post 2'},
#         {'id':3,'title':'Post 3','content':'Content of the Post 3'},
#         {'id':4,'title':'Post 4','content':'Content of the Post 4'},
#         {'id':5,'title':'Post 5','content':'Content of the Post 5'},
#         {'id':6,'title':'Post 6','content':'Content of the Post 6'}
#     ]

def index(request):
    blogs_title = 'Latest Posts'

    # Getting Data from Post Model
    all_posts=Post.objects.all()

    paginator = Paginator(all_posts,9)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    
    return render(request,'index.html',{'blogs_title':blogs_title,'page_obj':page_obj})

def detail(request,slug):
    #static Data
    # post = next((item for item in posts if item['id'] == post_id ),None)
    try:
        post=Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk = post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not found")

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post value is {post}')
    return render(request,'detail.html',{'post':post , "related_posts": related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the redirected new url")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        logger = logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f"The post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = 'Your message has been sent'
            return render(request, 'contact.html', {'form':form, 'success_message':success_message})
        else:
            logger.debug("Form validation is failed")
        return render(request,"contact.html",{"form":form,"success_message":success_message})
    return render(request,"contact.html")

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,"about.html",{'about_content':about_content})