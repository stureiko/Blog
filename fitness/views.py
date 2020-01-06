from django.shortcuts import render


def hello(request):
    return render(request, 'fitness/index.html')
