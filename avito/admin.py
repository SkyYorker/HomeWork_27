from django.contrib import admin

from ads.models import Ad
from cat.models import Category
from loc.models import Location
from user.models import User

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Ad)
