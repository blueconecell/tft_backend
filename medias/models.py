from django.db import models

class Photo(models.Model):
    file = models.URLField()
    description = models.TextField()
    champion = models.ForeignKey(
        "champions.Champion",
        on_delete = models.CASCADE,
        null=True,
        blank = True,
        related_name = "champion_photo",
    )
    skill = models.ForeignKey(
        "champions.Champion",
        on_delete = models.CASCADE,
        null=True,
        blank = True,
        related_name = "skill_photo",
    )
    job = models.ForeignKey(
        "synergies.Job",
        on_delete = models.CASCADE,
        null=True,
        blank = True,
        related_name = "job_photo",
    )
    origin = models.ForeignKey(
        "synergies.origin",
        on_delete = models.CASCADE,
        null=True,
        blank = True,
        related_name = "origin_photo",
    )
    item = models.ForeignKey(
        "items.Item",
        on_delete = models.CASCADE,
        null=True,
        blank = True,
        related_name = "item_photo",
    )
    augment = models.ForeignKey(
        "augments.Augment",
        on_delete = models.CASCADE,
        null=True,
        blank = True,
        related_name = "augment_photo",
    )

    def __str__(self) -> str:
        return "Photo File"
