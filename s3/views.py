# coding: utf-8
import boto3
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from s3.models import Upload


def list_files(request: HttpRequest) -> HttpResponse:
    uploads = Upload.objects.all()
    return render(request, "list.html", {"uploads": uploads})


def get_file(request: HttpRequest, pk: int) -> HttpResponse:
    if request.user.is_anonymous:
        raise PermissionError("nope")

    upload = get_object_or_404(Upload, pk=pk)

    url = _presigned_url(upload.file.name)

    return redirect(url)


def _presigned_url(name: str, expire=5):
    """expire in seconds"""
    s3_client = boto3.client("s3")

    # throws Exception in case of error
    response = s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
            "Key": name,
        },
        ExpiresIn=expire
    )

    return response
