from rest_framework.serializers import ModelSerializer

from medias.serializers import PhotoSerializer

from .models import Item

class ItemSerializer(ModelSerializer):
    item_photo = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = (
            "pk",
            "item_description",
            "item_effect",
            "item_photo",
        )
