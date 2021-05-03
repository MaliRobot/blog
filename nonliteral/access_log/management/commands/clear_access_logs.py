from django.core.management.base import BaseCommand, CommandError
import datetime
from django.utils import timezone
from flow.models import AccessLog


class Command(BaseCommand):

    help = 'Clean the user access logs older than x days'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        days_to_keep_data = 35
        now = timezone.now()
        back_date = now - datetime.timedelta(days=days_to_keep_data)
        AccessLog.objects.filter(timestamp__lt=back_date).delete()
