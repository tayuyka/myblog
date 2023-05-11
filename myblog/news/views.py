from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def news_home(request):
    news = Articles.objects.order_by('-date')
    paginator = Paginator(news, 4)  # 4 новости на странице
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом, отображаем первую страницу
        news = paginator.page(1)
    except EmptyPage:
        # Если параметр страницы больше, чем общее количество страниц, отображаем последнюю страницу
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма неверная"

    form = ArticlesForm()

    date = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', date)
