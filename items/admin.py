from django.contrib import admin

from items.models import Item

@admin.register(Item)
class OriginAdmin(admin.ModelAdmin):
    list_display=(
    # 이름
    "name", 

    # 아이템 아이콘

    # 아이템 설명
    "item_description",

    # 아이템 효과
    "item_effect",
    )