from django.db import models
from django.utils import timezone

class DataCall(models.Model):
    data_call = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.data_call}'

