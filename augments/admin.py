from django.contrib import admin

from augments.models import Augment

@admin.register(Augment)
class OriginAdmin(admin.ModelAdmin):
    list_display=(
    # 이름
    "name", 

    # 증강 아이콘

    # 증강 설명
    "augment_description",

    # 증강 티어
    "augment_tier",
    )