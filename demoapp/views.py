from django.http import HttpResponse
from . import tasks


# Create your views here.
def test_celery(request):
    tasks.slow_task.delay()
    return HttpResponse('Ok')
