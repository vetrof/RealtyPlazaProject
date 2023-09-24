from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    name_manager = models.CharField(max_length=50)
    email_manager = models.EmailField()
    id_realty = models.IntegerField()

    def __str__(self):
        return f'{self.message}'



