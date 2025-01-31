from uuid import uuid4

from django.db import models


class Item_State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Item_Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    state = models.ForeignKey(Item_State, on_delete=models.CASCADE)
    category = models.ForeignKey(Item_Category, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    image = models.ImageField(upload_to="items/")
    tags = models.ManyToManyField("Item_Tag", related_name="items")

    def __str__(self):
        return self.name


class Item_Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
