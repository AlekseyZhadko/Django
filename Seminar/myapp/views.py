from django.http import HttpResponse
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    context = {
        'title': 'Home'
    }
    logger.info(f'Result: home page access!')
    return render(request, 'games_app/index.html', context=context)


def about(request):
    context = {
        'title': 'About'
    }
    logger.info(f'Result: about page access')
    return render(request, 'games_app/about.html', context=context)
