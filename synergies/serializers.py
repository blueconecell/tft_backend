from rest_framework.serializers import ModelSerializer

from .models import Origin, Job

class OriginSerializer(ModelSerializer):
    class Meta:
        model = Origin
        fields = "__all__"

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"