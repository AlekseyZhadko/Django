from collections import Counter

from django.db import models


# Create your models here.
class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сторона: {self.is_eagle}, время: {self.create_at}'

    @staticmethod
    def counter(n: int):
        coins = Coin.objects.all().order_by('-create_at')[:n]
        coins_dict = {'orel': 0, 'reshka': 0}
        for coin in coins:
            if coin.is_eagle == 'orel':
                coins_dict['orel'] += 1
            else:
                coins_dict['reshka'] += 1
        # return [str(coin) + '<br>' for coin in coins][-n:]
        return coins_dict


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthday = models.DateField()

    def full_name(self):
        return f'{self.firstname} {self.lastname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return (f'title: {self.title},'
                f'description: {self.description},'
                f'create_at: {self.create_at},'
                f'author_id" {self.author_id},'
                f'category: {self.category},'
                f'views: {self.views},'
                f'publish: {self.publish}'
                )


class Comment(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now_add=True)