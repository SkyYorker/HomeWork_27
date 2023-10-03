# Generated by Django 4.2.4 on 2023-09-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('Пользователь', 'member'), ('admin', 'Админ'), ('Модератор', 'moderator')], default='member', max_length=12)),
                ('age', models.IntegerField(null=True)),
                ('locations', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
