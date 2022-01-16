# coding: utf-8
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from djauth.models import Upload


def list_files(request: HttpRequest) -> HttpResponse:
    uploads = Upload.objects.all()
    return render(request, "list.html", {"uploads": uploads})


def get_file(request: HttpRequest, pk: int) -> HttpResponse:
    if request.user.is_anonymous:
        raise PermissionError("nope")

    upload = get_object_or_404(Upload, pk=pk)
    response = HttpResponse()
    response.content = upload.file.read()
    response["Content-Disposition"] = "attachment; filename={0}".format(
        upload.file.name
    )
    return response
