# coding: utf-8
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.VERSION == "DJANGO":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    from djauth import views

    urlpatterns += [
        path("", views.list_files, name="list-files"),
        path("<int:pk>", views.get_file, name="get-file"),
    ]
elif settings.VERSION == "CADDY":
    from caddy import views

    urlpatterns += [
        path("", views.list_files, name="list-files"),
        path("<int:pk>", views.get_file, name="get-file"),
    ]
elif settings.VERSION == "S3":
    from s3 import views

    urlpatterns += [
        path("", views.list_files, name="list-files"),
        path("<int:pk>", views.get_file, name="get-file"),
    ]
