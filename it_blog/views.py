from django.shortcuts import render

def it_blog(request):
    return render(request, 'it_blog/it_blog.html')