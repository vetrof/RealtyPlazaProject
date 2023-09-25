from django.db import models
from django.utils import timezone

class DataCall(models.Model):
    data_call = models.DateTimeField(auto_now_add=True)
    chat_id = models.IntegerField(null=True, blank=True)
    login = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.data_call}'

