from rest_framework.serializers import ModelSerializer
from medias.serializers import PhotoSerializer
from .models import Origin, Job

class OriginSerializer(ModelSerializer):
    origin_photo = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Origin
        fields = "__all__"

class JobSerializer(ModelSerializer):

    job_photo = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = "__all__"