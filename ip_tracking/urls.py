from django.urls import path
from ip_tracking.views import RequestLogListAPIView, BlockedIpListAPIView

urlpatterns = [
    path("request/", RequestLogListAPIView.as_view(), name="requests ips"),
    path("blocked/", BlockedIpListAPIView.as_view(), name="blocked ips")
]
