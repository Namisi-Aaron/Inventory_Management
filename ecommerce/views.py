from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .filters import ItemFilter
from .forms import AddItemForm
from .models import Item

# items = [
#     {
#         "id": 1,
#         "name": "HP Laptop",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
#         "state": "new",
#         "category": "Laptop",
#         "purchase_date": "2025-01-12",
#         "image": "product1.jpg",
#         "tag": {"HP","COMPUTER"}
#     }
# ]


def home(request):
    items = Item.objects.order_by('-purchase_date')
    item_filter = ItemFilter(request.GET, queryset=items)
    context = {
        'filter': item_filter,
        'items': item_filter.qs,
    }
    return render(request, 'ecommerce/home.html', context)

def about(request):
    return render(request, 'ecommerce/about.html')

def add_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            item = form.save(commit=False)
            item.save()

            selected_tags = form.cleaned_data["tags"]
            item.tags.set(selected_tags)
            messages.success(request, "Item added successfully!")
            return redirect('ecom-home')
    else:
        form = AddItemForm()
    return render(request, 'ecommerce/add_item.html', {'form': form})

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            print(form.cleaned_data)
            item = form.save(commit=False)
            item.save()

            selected_tags = form.cleaned_data["tags"]
            item.tags.set(selected_tags)

            messages.success(request, "Item updated successfully!")
            return redirect('ecom-home')
    else:
        form = AddItemForm(instance=item)
    return render(request, 'ecommerce/update_item.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.success(request, "Item deleted successfully!")
    return redirect('ecom-home')
