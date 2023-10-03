from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __int__(self):
        return self.name
