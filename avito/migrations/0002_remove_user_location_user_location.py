# Generated by Django 4.2.4 on 2023-09-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(to='avito.location'),
        ),
    ]