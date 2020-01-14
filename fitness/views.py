from django.shortcuts import render


def hello(request):
    n = ['Test name', 'next name']
    left_panel_content = 'Текс левой панели'
    return render(request, 'fitness/index.html', context={'names': n, 'left_panel': left_panel_content})
