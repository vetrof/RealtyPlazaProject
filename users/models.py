from django.db import models




from django.db import models
from django.conf import settings

from realty.models import Realty


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_email = models.EmailField(blank=True, null=True)
    telegram_account = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


class Subscriber(models.Model):
    email = models.EmailField()


class Favorites(models.Model):
    realty = models.ForeignKey(Realty, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('realty', 'user')

    def __str__(self):
        return f'user {self.user.username}  -  {self.realty}'