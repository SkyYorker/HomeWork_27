import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Loads data from JSON'
    fixtures_dir = 'ads/fixtures'
    loaddata_command = 'loaddata'
    filenames = [
        "ad.json",
        "category.json",
        "loaction.json",
        "user.json",
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(self.loaddata_command, os.path.join(self.fixtures_dir, fixture_filename))
