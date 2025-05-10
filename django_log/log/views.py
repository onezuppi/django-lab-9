from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info('This is an information message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')

    return HttpResponse('Hello, world!')
