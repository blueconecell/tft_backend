from django.db import models

class Champion(models.Model):
    """챔피언 모델 정의"""

    # 챔피언 이름
    name = models.CharField(
        max_length=50,
        default = "챔피언"
    )

    # 챔피언 초상화 이미지

    # 가격
    price = models.PositiveIntegerField()

    # 계열
    origin = models.ManyToManyField(
        "synergies.Origin",
        related_name="champions"
    )

    # 직업
    job = models.ManyToManyField(
        "synergies.Job",
        related_name="champions"
    )
    
    # 체력
    health = models.PositiveIntegerField()

    # 공격력
    AD = models.PositiveIntegerField()

    # 사거리
    attack_range = models.PositiveIntegerField()

    # 공격속도
    attack_speed = models.FloatField()

    # DPS
    def DPS(self):
        return self.AD * self.attack_speed

    # 방어력
    armor = models.PositiveIntegerField()

    # 마법 저항력
    magic_resistance = models.PositiveIntegerField()

    # 스킬 이름
    skill_name = models.CharField(
        max_length=100,
        default = "스킬 이름"
    )
    
    # 스킬 초상화 이미지
    

    # 스킬 유형
    class SkillKindChoices(models.TextChoices):
        ACTIVE = "active", 'Active'
        PASSIVE = "passive", "Passive"
    skill_category = models.CharField(
        max_length=50,
        choices = SkillKindChoices.choices,
    )

    # 마나
    # 시작마나
    mana_start = models.IntegerField()
    # 총 마나
    mana_total = models.IntegerField()

    # 스킬 설명
    skill_description = models.TextField()

    # 스킬 효과
    skill_effect = models.TextField()

    def __str__(self) -> str:
        return self.name