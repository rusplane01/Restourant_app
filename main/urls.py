from django.urls import path
from .views import HomePage, RestaurantDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail')
]

app_name = 'main'