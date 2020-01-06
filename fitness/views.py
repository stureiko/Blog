from django.shortcuts import render


def hello(request):
    n = 'Test name'
    return render(request, 'fitness/index.html', context={'name': n})
