from django import forms
from .models import Item, Item_Category, Item_State, Item_Tag

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category', 'purchase_date', 'state', 'image', 'tags']

    category = forms.ModelChoiceField(
        queryset=Item_Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    state = forms.ModelChoiceField(
        queryset=Item_State.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Item_Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

# class AddItemForm(forms.Form):
#     name = forms.CharField(label='Product Name', max_length=100)
#     description = forms.CharField(label='Product Description', widget=forms.Textarea)
#     category_choices = [('laptop', 'Laptop'), ('monitor', 'Monitor'), ('mouse', 'Mouse'), ('CPU', 'CPU'), ('UPS', 'UPS'), ('keyboard', 'Keyboard')]
#     category = forms.ChoiceField(label='Product Category', choices=category_choices)
#     purchase_date = forms.DateField(label='Purchase Date')
#     state = forms.ChoiceField(label='State', choices=[('new', 'New'), ('used', 'Used'), ('refurbished', 'Refurbished')])
#     image = forms.ImageField(label='Product Image')
#     tag_choices = [('hp', 'HP'), ('samsung', 'SAMSUNG'), ('apple', 'APPLE'), ('computer', 'COMPUTER'), ('accessory', 'ACCESSORY'), ('dell', 'DELL'), ('lenovo', 'LENOVO')]
#     tags = forms.MultipleChoiceField(
#         label='Item Tags',
#         required=False,
#         choices=tag_choices,
#         widget=forms.CheckboxSelectMultiple()
#     )

#     def save(self):
#         item = Item(
#             name=self.cleaned_data['name'],
#             description=self.cleaned_data['description'],
#             category=self.cleaned_data['category'],
#             purchase_date=self.cleaned_data['purchase_date'],
#             state=self.cleaned_data['state'],
#             image=self.cleaned_data['image']
#         )
#         item.save()
#         return item
