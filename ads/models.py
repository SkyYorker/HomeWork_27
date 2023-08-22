from django.db import models

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Ads(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField( default=False)

# Create your models here.
