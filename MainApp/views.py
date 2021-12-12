from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

from .models import Pizza

def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user).order_by('date_added')
    context = {'pizzas':pizzas}

    return render(request, 'MainApp/pizzas.html',context)