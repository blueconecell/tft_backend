from django.contrib import admin

from synergies.models import Job, Origin

@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display=(
    # 이름
    "name", 

    # 계열 아이콘

    # 계열 설명
    "origin_description",

    # 계열 효과
    "origin_effect",
    )

@admin.register(Job)
class OriginAdmin(admin.ModelAdmin):
    list_display=(
    # 이름
    "name", 

    # 계열 아이콘

    # 계열 설명
    "job_description",

    # 계열 효과
    "job_effect",
    )