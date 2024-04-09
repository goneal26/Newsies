# rss feed fetching, with help
# from https://stackoverflow.com/questions/70859953/how-to-update-my-django-database-with-rss-feed-every-x-minutes

import feedparser
from .models import Outlet, Blurb

class RSSFetcher:

	@staticmethod
	def update_db():
		pass 

	@staticmethod
	def fetch_one(url):
		pass