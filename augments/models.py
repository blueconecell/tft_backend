from django.db import models

class Augment(models.Model):
    
    # 이름
    name = models.CharField(
        max_length=100,
    )

    # 증강 아이콘

    # 증강 설명
    augment_description = models.TextField()

    # 증강 티어
    class AugmentTierKindChoice(models.TextChoices):
        SILVER = "silver","Silver"
        GOLD = "gold", "Gold"
        PRISM = "prism","Prism"
    augment_tier = models.CharField(
        max_length=50,
        choices = AugmentTierKindChoice.choices,
        default = AugmentTierKindChoice.SILVER,
    )

    def __str__(self) -> str:
        return self.name