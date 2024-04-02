from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'title': 'Home', 'articles': articles})


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/edit_article.html', {'form': form, 'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    return render(request, 'main/delete_article.html', {'article': article})


