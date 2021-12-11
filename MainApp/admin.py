from django.contrib import admin

# Register your models here.
from .models import Pizza,Topings

admin.site.register(Pizza)
admin.site.register(Topings)