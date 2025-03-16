from celery import Celery

sandwich = Celery("tasks",  broker="pyamqp://guest@localhost//", backend="rpc://" )

@sandwich.task
def power(n, power):
    return n ** power