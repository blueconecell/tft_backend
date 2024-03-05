from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ItemSerializer
from .models import Item

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return Response(items_serializer.data)