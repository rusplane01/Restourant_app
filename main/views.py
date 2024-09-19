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


def dishes(request, category_id=None):
    context = {'categories': models.Category.objects.all()}
    if category_id:
        context.update({'dishes': models.Dish.objects.filter(category_id=category_id)})
    else:
        context.update({'dishes': models.Dish.objects.all()})
    return render(request, 'main/restaurant_detail.html', context)


class DishDetailView(DetailView):
    model = models.Dish
    context_object_name = 'dish'
    template_name = 'main/dish_detail.html'


def basket_view(request):
    user = request.user
    context = {
        'baskets': models.Basket.objects.filter(user=request.user)
    }
    return render(request, 'main/basket.html', context)

def basket_add(request, dish_id):
    current_page = request.META.get('HTTP_REFERER')
    dish = models.Dish.objects.get(id=dish_id)
    baskets = models.Basket.objects.filter(user=request.user, dish=dish)

    if not baskets.exists():
        models.Basket.objects.create(user=request.user, dish=dish, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        if basket is not None:
            basket.quantity += 1
            basket.save()
            return HttpResponseRedirect(current_page)


def basket_remove(request, id):
    basket = models.Basket.objects.get(id=id)
    basket.quantity -= 1
    basket.save()
    if basket.quantity < 1:
        basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))







