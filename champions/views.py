from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .serializers import ChampionSerializer,ChampionListSerializer
from .models import Champion

class Champions(APIView):
    def get(self,request):
        champions = Champion.objects.all()
        serializer = ChampionListSerializer(champions, many=True)
        return Response(serializer.data)
    


class ChampionDetails(APIView):
    def get_object(self, pk):
        try:
            return Champion.objects.get(pk=pk)
        except Champion.DoesNotExist:
            raise NotFound
        
    def get(self, request, pk):
        champion = self.get_object(pk)
        serializer = ChampionSerializer(champion)
        return Response(serializer.data)

