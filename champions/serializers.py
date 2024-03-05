from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Champion


class ChampionSerializer(ModelSerializer):
    DPS = serializers.SerializerMethodField()
    def get_DPS(self,champion):
        return champion.DPS()
    class Meta:
        model = Champion
        fields = "__all__"

class ChampionListSerializer(ModelSerializer):
    # 챔피언 초상화

    # 스킬 초상화

    # 계열 초상화

    # 직업 초상화
    
    class Meta:
        model = Champion
        fields = (
            "id",
            "name",
            "price",
            "health",
            "AD",
            "attack_range",
            "attack_speed",
            "DPS",
            "armor",
            "magic_resistance",
            "skill_name",
            "skill_category",
            "mana_start",
            "mana_total",
            "skill_description",
            "skill_effect",
            "origin",
            "job",
            
        )