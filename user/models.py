from django.db import models
from django.contrib.auth.models import AbstractUser
from loc.models import Location
from user.validators import check_date_for_user, check_email_for_user


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Админ'),
        (MODERATOR, 'Модератор'),
    )


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=12, choices=UserRoles.choices, default='member')
    age = models.IntegerField(null=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_date_for_user])
    email = models.EmailField(unique=True, validators=[check_email_for_user])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name, self.last_name
