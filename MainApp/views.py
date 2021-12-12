from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

from .models import Pizza

def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizzas':pizzas}

    return render(request, 'MainApp/pizzas.html',context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')

    context = {'pizza': pizza, 'toppings': toppings, 'comments': comments}
    return render(request, 'pizzas/pizzas.html', context)
