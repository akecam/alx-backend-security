from rest_framework import generics
from ip_tracking.models import RequestLog, BlockedIP
from ip_tracking.serializers import RequestLogSerializer, BlockedIpSerializer

class RequestLogListAPIView(generics.ListAPIView):

     queryset = RequestLog.objects.all()
     serializer_class = RequestLogSerializer


class BlockedIpListAPIView(generics.ListAPIView):

    queryset = BlockedIP.objects.all()
    serializer_class = BlockedIpSerializer
