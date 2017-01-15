from django.shortcuts import render
from blogs.models import blogPost
from  django.core.exceptions import ObjectDoesNotExist
 # django.core.exceptions.ObjectDoesNotExist

def zawijanie(request):
    context = {}
    return render(request, 'zwijanie_menu.html', context)

def sidebar(request):
    posts = blogPost.objects.all().order_by('-views_count')[:10]
    context = {'posts': posts}
    return render(request, 'sidebar.html', context)  
      
def about(request):
    context = {}
    return render(request, 'blog_template.html', context)

def blob(request):
    posts = blogPost.objects.all()
    context = {'posts': posts, 'blog_main' : True, 'blog': 'blob'}
    return render(request, 'blog_template.html', context)

def post(request, article_link = None):
    post = blogPost.objects.get(article_link = article_link)
    post.views_count += 1
    post.save()
    # import pdb
    # pdb.set_trace()
    prev_post = blogPost.objects.get(article_link = article_link, blog = post.blog)
    next_post = prev_post
    
    prev_post = blogPost.objects.get_previous_blog_post(prev_post)
    next_post = blogPost.objects.get_next_blog_post(next_post)

    context = {
        'post': post, 
        'blog': post.blog, 
        'next': next_post, 
        'previous': prev_post
    }
    return render(request, 'blog_template.html', context)

def it_blog(request):
    posts = blogPost.objects.filter(blog='it')
    context = {'posts': posts, 'blog_main' : True, 'blog': 'it'}
    return render(request, 'blog_template.html', context)

def moto(request):
    posts = blogPost.objects.filter(blog='moto')
    context = {'posts': posts, 'blog_main' : True, 'blog': 'moto'}
    return render(request, 'blog_template.html', context)
