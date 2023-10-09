from django.db import models

from ads.models import Ad
from user.models import User


# Create your models here.
class Selection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка Обьявлений"
        verbose_name_plural = "Подборка обьявления"

    def __str__(self):
        return self.name
