from celery import shared_task
from tbot.models import DataCall
from tbot.parser.parser import parsing


@shared_task
def my_task():
    parsing()

