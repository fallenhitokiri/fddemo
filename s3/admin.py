# coding: utf-8
from django.contrib import admin

from s3.models import Upload


admin.site.register(Upload)
