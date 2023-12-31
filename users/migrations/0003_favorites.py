# Generated by Django 4.2.5 on 2023-09-25 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0006_alter_realty_house'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realty.realty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
