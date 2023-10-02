import random

from django.shortcuts import render
from django.http import HttpResponse
import logging

from myapp2.models import Coin

logger = logging.getLogger(__name__)


# Create your views here.
def eagle(request, count: int):
    game_list = ['orel', 'reshka']
    result = []
    for i in range(count + 1):
        response = random.choice(game_list)
        result.append(response)

    context = {
        'result': result
    }
    # coin = Coin(is_eagle=response)
    # coin.save()
    # logger.info(f'Result: {coin}')
    return render(request, 'myapp/index.html', context=context)


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
