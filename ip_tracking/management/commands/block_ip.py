from ip_tracking.models import BlockedIP
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        BLOCKED_IP = [
            '127.0.0.1'
        ]
        try:
            for ip_addr in BLOCKED_IP:
                BlockedIP.objects.create(ip_address=ip_addr)
        except Exception as e:
            print(f"Couldn't store an ip_addr {e}")
        finally:
            print("Completed")
