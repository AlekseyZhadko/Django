from django.http import HttpResponse
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info(f'Result: home page access!')
    return HttpResponse('<h1>Home page</h1>'
                        '<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa et ut tenetur recusandae minima. '
                        'Quibusdam numquam dolore omnis dicta eum voluptas, vel error dolorum odio cumque eveniet quod? Architecto, '
                        'deleniti.'
                        '</p>'
                        )


def about(request):
    logger.info(f'Result: about page access')
    return HttpResponse('<h1>About page</h1>'
                        '<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa et ut tenetur recusandae minima. '
                        'Quibusdam numquam dolore omnis dicta eum voluptas, vel error dolorum odio cumque eveniet quod? Architecto, '
                        'deleniti.'
                        '</p>'
                        )
