from django.urls import path

from myapp2 import views

urlpatterns = [
    path('articles/<int:author_id>', views.get_articles, name='get_articles'),
    path('detail/<int:article_id>', views.detail_articles, name='detail_articles'),
    path('add_author/', views.author, name='author'),
    path('add_article/', views.article, name='article'),
]
