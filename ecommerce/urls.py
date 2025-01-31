from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="ecom-home"),
    path("categories", views.categories, name="ecom-categories"),
    path("about/", views.about, name="ecom-about"),
    path("add-item/", views.add_item, name="ecom-add-item"),
    path("add-category/", views.add_category, name="ecom-add-category"),
    path("add_tag/", views.add_tag, name="ecom-add-tag"),
    path("item/<uuid:item_id>/update/", views.update_item, name="ecom-update-item"),
    path(
        "category/<uuid:category_id>/update/",
        views.update_category,
        name="ecom-update-category",
    ),
    path("item/<uuid:item_id>/delete/", views.delete_item, name="ecom-delete-item"),
    path(
        "category/<uuid:category_id>/delete/",
        views.delete_category,
        name="ecom-delete-category",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
