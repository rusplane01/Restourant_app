from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # уникуе
    def __str__(self):
        return f'{self.name}'


class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    rate = models.IntegerField()
    place = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/")

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

    def __str__(self):
        return f'{self.restaurant} - {self.main_reason}'




