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
def slow_task():
    print('Started task, processing...')
    time.sleep(120)
    print('Finished Task')
    return True
