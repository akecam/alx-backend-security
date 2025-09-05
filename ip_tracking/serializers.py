from rest_framework import serializers
from ip_tracking.models import RequestLog, BlockedIP


class RequestLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestLog
        fields = "__all__"


class BlockedIpSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockedIP
        fields = "__all__"
