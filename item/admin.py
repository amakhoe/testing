from django.contrib import admin
from .models import Categoria
from .models import Item

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Item)
