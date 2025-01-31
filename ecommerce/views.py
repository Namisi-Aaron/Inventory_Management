from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .filters import CategoryFilter, ItemFilter
from .forms import AddCategoryForm, AddItemForm, AddTagForm
from .models import Item, Item_Category

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
    items = Item.objects.order_by("-purchase_date")
    item_filter = ItemFilter(request.GET, queryset=items)
    context = {
        "filter": item_filter,
        "items": item_filter.qs,
    }
    return render(request, "ecommerce/home.html", context)


def categories(request):
    categories = Item_Category.objects.order_by("name")
    category_filter = CategoryFilter(request.GET, queryset=categories)
    context = {
        "filter": category_filter,
        "categories": category_filter.qs,
    }
    return render(request, "ecommerce/categories.html", context)


def about(request):
    return render(request, "ecommerce/about.html")


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
            return redirect("ecom-home")
    else:
        form = AddItemForm()
    return render(request, "ecommerce/add_item.html", {"form": form})


def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect("ecom-home")
    else:
        form = AddCategoryForm()
    return render(request, "ecommerce/add_category.html", {"form": form})


def add_tag(request):
    if request.method == "POST":
        form = AddTagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag added successfully!")
            return redirect("ecom-home")
    else:
        form = AddTagForm()
    return render(request, "ecommerce/add_tag.html", {"form": form})


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
            return redirect("ecom-home")
    else:
        form = AddItemForm(instance=item)
    return render(request, "ecommerce/update_item.html", {"form": form})


def update_category(request, category_id):
    category = get_object_or_404(Item_Category, id=category_id)

    if request.method == "POST":
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect("ecom-categories")
    else:
        form = AddCategoryForm(instance=category)
    return render(request, "ecommerce/update_category.html", {"form": form})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.success(request, "Item deleted successfully!")
    return redirect("ecom-home")


def delete_category(request, category_id):
    category = get_object_or_404(Item_Category, id=category_id)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect("ecom-categories")
