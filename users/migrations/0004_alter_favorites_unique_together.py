# Generated by Django 4.2.5 on 2023-09-25 13:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0006_alter_realty_house'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_favorites'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('realty', 'user')},
        ),
    ]
