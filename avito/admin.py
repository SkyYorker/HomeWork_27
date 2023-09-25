from django.contrib import admin
from avito.models import Category, Location, User, Ad
# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Ad)
