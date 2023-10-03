import random

from django.shortcuts import render
from django.http import HttpResponse
import logging

from games_app.forms import Games
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
    return render(request, 'games_app/index.html', context=context)


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


def games(request):
    if request.method == 'POST':
        form = Games(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            count = form.cleaned_data['count']
            logger.info(f'Получили {name=}, {count=}.')

            if name == 'E':
                return HttpResponse(f'{Coin.counter(count)}')
    else:
        form = Games()
    return render(request, 'games_app/add_author.html', {'form': form})
