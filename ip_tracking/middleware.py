import logging
from ip_tracking.models import BlockedIP, RequestLog
from django.http import HttpResponseServerError


logger = logging.getLogger('ip_tracking.middleware')

class IPLoggingMiddleware:

    def __init__(self, get_respose):
        self.get_response = get_respose

    def __call__(self, request):

        logger.info(f"{request.path} {request.META.get('REMOTE_ADDR')}")
        RequestLog.objects.create(ip_address=request.META.get('REMOTE_ADDR'), path=request.path)

        response = self.get_response(request)

        return response


class IPAddressBlocked:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        if BlockedIP.objects.filter(ip_address=request.META.get('REMOTE_ADDR')).exists():
            response = HttpResponseServerError("Oops Something went wrong.")
            return response
        else:
            response = self.get_response(request)
            return response
