# Generated by Django 3.1.3 on 2020-11-17 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sand1', '0003_auto_20201118_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(),
        ),
    ]