import random

from django.shortcuts import render
from django.http import HttpResponse
import logging

from myapp2.models import Coin

logger = logging.getLogger(__name__)


# Create your views here.
def eagle(request):
    game_list = ['orel', 'reshka']
    response = random.choice(game_list)
    coin = Coin(is_eagle=response)
    coin.save()
    logger.info(f'Result: {coin}')
    return HttpResponse(coin)


def show_elements(request, n: int):
    return HttpResponse(f'{Coin.counter(n)}')


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Result: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    random_number_value = random.randint(0, 100)
    logger.info(f'Result: {random_number_value}')
    return HttpResponse(random_number_value)
