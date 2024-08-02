from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    rate = models.IntegerField()
    place = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
    

class Dish(models.Model):
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=250)
    description = models.TextField()




