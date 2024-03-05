from django.db import models

# 계열
class Origin(models.Model):
    
    # 이름
    name = models.CharField(
        max_length=100,
    )

    # 계열 아이콘

    # 계열 설명
    origin_description = models.TextField()

    # 계열 효과
    origin_effect = models.TextField()

    def __str__(self) -> str:
        return self.name
    


class Job(models.Model):
    
    # 이름
    name = models.CharField(
        max_length=100,
    )

    # 직업 아이콘

    # 직업 설명
    job_description = models.TextField()

    # 직업 효과
    job_effect = models.TextField()

    def __str__(self) -> str:
        return self.name