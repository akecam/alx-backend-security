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


class IPAddressBloocked:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):


        try:
            blocked_ip = BlockedIP.objects.get(ip_address=request.META.get('REMOTE_ADDR'))
            if blocked_ip.DoesNotExist:
                raise Exception
            response = self.get_response(request)
        except Exception as e:
            response = HttpResponseServerError("Oops! Something went wrong.")
        return response
