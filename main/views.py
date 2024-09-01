from django.shortcuts import render, redirect, HttpResponseRedirect
from main import models
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


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
            comment.author = request.user
            comment.save()
            return redirect('main:restaurant_detail', pk=comment.restaurant.pk)
        else:
            # Тут можна обробити випадок з невалідною формою
            pass

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get("category", "")
        if category:
            queryset = queryset.filter(category=category)
        return queryset
        

class MenuListView(ListView):
    model = models.Dish
    context_object_name = 'dishes'
    template_name = 'main/restaurant_detail.html'


class DishDetailView(DetailView):
    model = models.Dish
    context_object_name = 'dish'
    template_name = 'main/dish_detail.html'


def basket_view(request):
    user = request.user
    context = {
        'baskets': basket.objects.filter(user=request.user)
    }
    return render(request, 'main/basket.html', context)

def basket_ad(request, dish_id):
    current_page = request.Meta.get('HTTP_REFERER')
    dish = Dish.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, dish=dish)

    if not baskets.exsists:
        Basket.objects.create(user=request.user, dish=dish, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity == 1
        basket.save()
        return HttpResponseRedirect(current_page)





