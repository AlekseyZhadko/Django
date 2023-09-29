import datetime
import random

from django.core.management.base import BaseCommand
from myapp2.models import Author, Article


class Command(BaseCommand):
    help = "Generate fake authors and article."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(firstname=f'firstname{i}',
                            lastname=f'lastname{i}',
                            email=f'mail{i}@mail.ru',
                            biography=f'biography{i}',
                            birthday=datetime.date(1997, 10, 19), )
            author.save()
            for j in range(1, count + 1):
                article = Article(title=f'Title{j}',
                                  description=f'Text from {author.full_name()}  # {j} is bla bla bla many long text',
                                  author_id=author,
                                  category=f'category{j}',
                                  views=random.randint(1, 200),
                                  publish=random.choice([True, False]), )
                article.save()
