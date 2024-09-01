from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('<int:pk>/menu/', views.MenuListView.as_view(), name='menu_list'),
    path('<int:pk>/detail/', views.DishDetailView.as_view(), name='dish_detail'),
    path('basket/', views.BasketView.as_view(), name='basket'),
]

app_name = 'main'