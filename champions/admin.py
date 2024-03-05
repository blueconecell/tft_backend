from django.contrib import admin
from .models import Champion

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    def get_origins_display(self, obj):
        return ", ".join([origin.name for origin in obj.origin.all()])
    get_origins_display.short_description = 'Origins'

    def get_jobs_display(self, obj):
        return ", ".join([job.name for job in obj.job.all()])
    get_jobs_display.short_description = 'Jobs'
    list_display = (
    # 챔피언 이름
    "name",
    # 챔피언 초상화 이미지
    # 가격
    "price",
    # 계열
    "get_origins_display",
    # 직업
    "get_jobs_display",
    # 체력
    "health",
    # 공격력
    "AD",
    # DPS
    "DPS",
    # 사거리
    "attack_range",
    # 공격속도
    "attack_speed",
    # 방어력
    "armor",
    # 마법 저항력
    "magic_resistance",
    # 스킬 이름
    "skill_name",
    # 스킬 초상화 이미지
    
    # 스킬 유형
    "skill_category", 
    # 마나
    # 시작마나
    "mana_start",
    # 총 마나
    "mana_total",
    # 스킬 설명
    "skill_description",
    # 스킬 효과
    "skill_effect",
    )
    list_filter = (
        "name",
        "price",
    )