# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def test():
    print('Olha eu aqui!')


@shared_task
def slow_task():
    time.sleep(5)
    print('+>>>>>> Slow after 5 seconds')
