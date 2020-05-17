import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until DB is ready"""

    def handle(self, *args, **options):
        """Check if the DB is ready first"""
        self.stdout.write('Waiting for the DB')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available!'))