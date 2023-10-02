from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from myapp2.models import Article, Author, Comment


# Create your views here.

def get_articles(request, author_id: int):
    articles = Article.objects.filter(author_id=author_id)
    context = {
        'articles': articles
    }
    return render(request, 'myapp/index.html', context=context)


def detail_articles(request, article_id):
    articles = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('-change_at')
    articles.views += 1
    articles.save()
    print(articles)
    context = {
        'articles': articles,
        'comments': comments
    }
    return render(request, 'myapp/about.html', context=context)
