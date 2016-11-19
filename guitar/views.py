from django.shortcuts import render

def guitar(request):
    return render(request, 'guitar/guitar.html')
