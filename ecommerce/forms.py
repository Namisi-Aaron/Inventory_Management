from django import forms

from .models import Item, Item_Category, Item_State, Item_Tag


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "description",
            "category",
            "purchase_date",
            "state",
            "image",
            "tags",
        ]

    category = forms.ModelChoiceField(
        queryset=Item_Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    state = forms.ModelChoiceField(
        queryset=Item_State.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Item_Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Item_Category
        fields = ["name"]


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Item_Tag
        fields = ["name"]
