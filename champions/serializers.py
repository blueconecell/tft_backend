from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from medias.serializers import PhotoSerializer
from synergies.serializers import OriginSerializer,JobSerializer

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
    champion_photo = PhotoSerializer(many=True, read_only=True) 
    # 스킬 초상화
    skill_photo = PhotoSerializer(many=True, read_only=True)
    # 계열
    origin = OriginSerializer(many=True, read_only=True)
    # 계열 초상화
    origin_photo = PhotoSerializer(many=True, read_only=True)
    # 직업
    job = JobSerializer(many=True, read_only=True)
    # 직업 초상화
    job_photo = PhotoSerializer(many=True, read_only=True)
    
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
            "champion_photo",
            "skill_photo",
            "origin_photo",
            "job_photo",
        )