from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AugmentSerializer
from .models import Augment

class AugmentList(APIView):
    def get(self, request):
        augments = Augment.objects.all()
        augments_serializer = AugmentSerializer(augments, many=True)
        return Response(augments_serializer.data)