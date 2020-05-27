# Celery how to's

## REDIS
Make sure that redis is up before try celery tasks running:

`sudo systemctl status redis`

## Start celery worker
`celery worker --app=celerysample --loglevel=info`

## Start celery beat
`celery beat --app=celerysample --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler`  

## Start celery worker with beat (For development only)
`celery worker --app=celerysample --loglevel=info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler`
