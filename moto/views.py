from django.shortcuts import render

def moto(request):
    return render(request, 'moto/moto.html')