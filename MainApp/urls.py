from django.urls import path

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('Pizzas', views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>/',views.pizzas,name='pizza')

]