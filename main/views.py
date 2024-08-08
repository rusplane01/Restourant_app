from django.shortcuts import render
from main import models
from django.views.generic import ListView


class RestaurantListView(ListView):
    model = models.Restaurant
    context_object_name = "Restaurants"
    template_name = "main/home.html"

