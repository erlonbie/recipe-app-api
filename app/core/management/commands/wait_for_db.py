"""
Django command to wait for the database to be available before starting
the server.
"""

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database"""

    def handle(self, *args, **options):
        """Entry point for the command."""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True  # Simulate successful database connection
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 2 second...")
                time.sleep(2)
        self.stdout.write(self.style.SUCCESS("Database available!"))
