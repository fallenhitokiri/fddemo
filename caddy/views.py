# coding: utf-8
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings

from caddy.models import Upload


def list_files(request: HttpRequest) -> HttpResponse:
    uploads = Upload.objects.all()
    return render(request, "list.html", {"uploads": uploads})


def get_file(request: HttpRequest, pk: int) -> HttpResponse:
    if request.user.is_anonymous:
        raise PermissionError("nope")

    upload = get_object_or_404(Upload, pk=pk)
    fqp = upload.file.path
    rel = fqp.split(settings.MEDIA_ROOT)[1]
    response = HttpResponse()
    response["X-Accel-Redirect"] = rel
    return response
