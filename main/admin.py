from django.contrib import admin
from .models import Dish, Restaurant, Category, Comment

admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Comment)
