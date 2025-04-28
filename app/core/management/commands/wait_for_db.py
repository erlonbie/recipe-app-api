"""
Django command to wait for the database to be available before starting the server.
"""

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be available before starting the server."""

    def handle(self, *args, **options):
        """Entry point for the command."""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                # Simulate a database check
                # In a real scenario, you would use Django's database connection here
                # For example: from django.db import connection
                # connection.ensure_connection()
                self.check(databases=["default"])
                db_up = True  # Simulate successful database connection
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 2 second...")
                time.sleep(2)
        self.stdout.write(self.style.SUCCESS("Database available!"))

    # def check(self):
    #     pass
    #     # """Check if the database is available."""
    #     # try:
    #     #     self.stdout.write("Checking database connection...")
    #     #     # Simulate a database check
    #     #     # In a real scenario, you would use Django's database connection here
    #     #     # For example: from django.db import connection
    #     #     # connection.ensure_connection()
    #     #     self.stdout.write(self.style.SUCCESS("Database is available!"))
    #     # except Exception as e:
    #     #     self.stdout.write(self.style.ERROR(f"Database is not available: {e}"))
