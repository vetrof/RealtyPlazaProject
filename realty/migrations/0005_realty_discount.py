# Generated by Django 4.2.5 on 2023-09-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0004_alter_realty_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='realty',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]