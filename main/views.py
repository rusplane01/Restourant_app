from django.shortcuts import render, redirect
from main import models
from .forms import CommentForm
from django.views.generic import ListView, DetailView


class HomePage(ListView):
    model = models.Restaurant
    context_object_name = "restaurants"
    template_name = "main/home.html"


class RestaurantDetailView(DetailView):
    model = models.Restaurant
    context_object_name = "restaurant"
    template_name = 'main/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Додаємо порожню форму коментаря в контекст
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.restaurant = self.get_object() 
            comment.save()
            return redirect('main:restaurant_detail', pk=comment.restaurant.pk)
        else:
            # Тут можна обробити випадок з невалідною формою
            pass


class CategoryListView(ListView):
    model = models.Category 
    template_name = 'main/category_list.html'


class MenuListView(ListView):
    model = models.Dish
    context_object_name = 'dishes'
    template_name = 'main/menu_list.html'
    