import django_filters

from .models import Item, Item_Category


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Item
        fields = ["name", "category", "tags"]


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Item_Category
        fields = ["name"]
