# Generated by Django 4.2.4 on 2023-10-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loc', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.AddField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(to='loc.location'),
        ),
    ]
