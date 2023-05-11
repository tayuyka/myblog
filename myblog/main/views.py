from django.shortcuts import render
from django.shortcuts import render
# from .models import Post


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})


def index(request):
    data = {'title': 'Главная страница',
            'values': ['Some', 'Hello', '123']}
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')