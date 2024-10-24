from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .form import NewItem, EditItem

# display each item
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(categoria=item.categoria, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required
def newAdd(request):
    if request.method == 'POST':
        form = NewItem(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail.html', pk=item.id)
    else:
        form = NewItem()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Novo Item'
    })

@login_required
def newEdit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItem(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail.html', pk=item.id)
    else:
        form = EditItem(instance=item)
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Editar Item'
    })


def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('item:detail.html')