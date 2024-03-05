from django.db import models

class Item(models.Model):
    
    # 이름
    name = models.CharField(
        max_length=100,
    )

    # 아이템 아이콘

    # 아이템 설명
    item_description = models.TextField()

    # 아이템 효과
    item_effect = models.TextField()

    def __str__(self) -> str:
        return self.name