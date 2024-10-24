from django.shortcuts import render, redirect
from item.models import Categoria, Item
from .forms import RegistroForm

# home page
def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    Categorias = Categoria.objects.all()
    return render(request, 'core/index.html', {
        'categorias': Categorias,
        'items': items,
    })

def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = RegistroForm()

    return render(request, 'core/registro.html', {
        'form': form
    })