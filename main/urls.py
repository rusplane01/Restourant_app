from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantListView, name='restaurants_list'),
]

app_name = 'main'