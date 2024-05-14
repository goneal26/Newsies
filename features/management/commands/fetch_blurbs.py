from django.core.management.base import BaseCommand
from features.rss import RSSFetcher

class Command(BaseCommand):
    help = 'Fetches all blurbs via RSS fetcher class'

    def handle(self, *args, **options):
        RSSFetcher.update_db()