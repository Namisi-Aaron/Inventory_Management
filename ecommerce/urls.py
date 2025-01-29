from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="ecom-home"),
    path("about/", views.about, name="ecom-about"),
    path("add-item/", views.add_item, name="ecom-add-item"),
    path("item/<uuid:item_id>/update/", views.update_item, name="ecom-update-item"),
    path("item/<uuid:item_id>/delete/", views.delete_item, name="ecom-delete-item"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
