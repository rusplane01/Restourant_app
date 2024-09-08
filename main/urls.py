from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('<int:pk>/restaurant/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('<int:category_id>/', views.dishes, name='category'),

    path('<int:pk>/detail/', views.DishDetailView.as_view(), name='dish_detail'),
    path('basket/', views.basket_view, name='basket'),
    path('basket_add/<int:dish_id>/', views.basket_add, name='basket_add'),
    path('basket_remove/<int:id>/', views.basket_remove, name='basket_remove'),
]

app_name = 'main'