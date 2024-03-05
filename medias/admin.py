from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
    "file",
    "description",
    "champion",
    "job",
    "origin",
    "item",
    "augment",
    )
