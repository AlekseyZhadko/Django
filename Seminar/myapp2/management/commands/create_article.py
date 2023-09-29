import random

from django.core.management.base import BaseCommand
from myapp2.models import Article, Author


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        article = Article(title=f'Title 20',
                          description=f'Text from # 20 is bla bla bla many long text',
                          author_id=Author,
                          category=f'category 20',
                          views=random.randint(1, 200),
                          publish=random.choice([True, False]), )
        article.save()
        self.stdout.write(f'{article}')
