from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OriginSerializer, JobSerializer
from .models import Origin, Job

class OriginList(APIView):
    def get(self, request):
        origins = Origin.objects.all()
        origins_serializer = OriginSerializer(origins, many=True)
        return Response(origins_serializer.data)
    
class JobList(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        jobs_serializer = JobSerializer(jobs, many=True)
        return Response(jobs_serializer.data)
