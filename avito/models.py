from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    
    # def __int__(self):
    #     return self.id
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    


    class Meta():
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        ('Пользователь', USER),
        ('Админ', ADMIN),
        ('Модератор', MODERATOR),
    )

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=12, choices=UserRoles.choices, default='member')
    age = models.IntegerField()
    locations = models.ManyToManyField(Location)

    class Meta():
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __int__(self):
        return self.first_name, self.last_name
    

class Ad(models.Model):
    Id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'

    def __str__(self):
        return self.name