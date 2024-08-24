from django.urls import path
from .views import HomePage, RestaurantDetailView, MenuListView, DishDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('<int:pk>/menu/', MenuListView.as_view(), name='menu_list'),
    path('<int:pk>/detail/', DishDetailView.as_view(), name='dish_detail'),
]

app_name = 'main'