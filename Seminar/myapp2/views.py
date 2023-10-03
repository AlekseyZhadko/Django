from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from myapp2.forms import Author_form, Article_form
from myapp2.models import Article, Author, Comment


# Create your views here.

def get_articles(request, author_id: int):
    articles = Article.objects.filter(author_id=author_id)
    context = {
        'articles': articles
    }
    return render(request, 'myapp2/index.html', context=context)


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


def author(request):
    if request.method == 'POST':
        form = Author_form(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(firstname=firstname,
                            lastname=lastname,
                            email=email,
                            biography=biography,
                            birthday=birthday,
                            )
            author.save()
    else:
        form = Author_form()
    return render(request, 'myapp2/add_author.html', {'form': form})


def article(request):
    if request.method == 'POST':
        form = Article_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            author_id = form.cleaned_data['author']
            category = form.cleaned_data['category']
            publish = form.cleaned_data['publish']
            author = get_object_or_404(Author, id=int(author_id))
            article = Article(title=title,
                              description=description,
                              author_id=author,
                              category=category,
                              publish=publish,
                              )
            article.save()
    else:
        form = Article_form()
    return render(request, 'myapp2/add_article.html', {'form': form})
