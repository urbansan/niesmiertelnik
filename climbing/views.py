from django.shortcuts import render

def climbing(request):
    return render(request, 'climbing/climbing.html')