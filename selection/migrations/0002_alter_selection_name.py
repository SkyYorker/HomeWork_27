# Generated by Django 4.2.4 on 2023-10-09 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
