from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    rate = models.IntegerField()
    description = models.TextField()
    place = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # уникуе
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default='1', related_name='categories')

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    

class Comment(models.Model):
    main_reason = models.CharField(max_length=250)
    text = models.TextField()
    rate = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='authors')

    def __str__(self):
        return f'{self.restaurant} - {self.main_reason}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'basket for {self.user.username}'



