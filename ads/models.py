from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from cat.models import Category
from user.models import User


class Ad(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

    def __str__(self):
        return self.name