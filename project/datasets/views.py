from django.shortcuts import render


def index(request):
    return render(request, 'datasets/index.html',
                  context={'username': request.user.username})
