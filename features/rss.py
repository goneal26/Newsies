# rss feed fetching, with help
# from https://stackoverflow.com/questions/70859953/how-to-update-my-django-database-with-rss-feed-every-x-minutes
# also based on the scratch file I wrote

import feedparser
from datetime import datetime, timedelta
from dateutil import parser
from django.utils.timezone import make_aware
import pytz
from .models import Outlet, Blurb

class RSSFetcher:

	@staticmethod
	def update_db():
		""" Static method for updating blurbs in the database.
		"""
		for outlet in Outlet.objects.all():
			feed_list = RSSFetcher.fetch_one(outlet.rss_url)
			for feed_item in feed_list:
				new_blurb = Blurb.create(feed_item, outlet)
				new_blurb.save() # saves new blurb obj to db

	@staticmethod
	def fetch_one(url):
		"""Fetches all of today's RSS feed for one outlet.

		Keyword arguments:
		url -- the RSS feed url for that outlet.
		
		Return: a list of dictionary objects representing blurb entries. 
		"""
		now = datetime.now().astimezone(pytz.utc)
		time_range = timedelta(days=1)
		feed = feedparser.parse(url)
		blurb_list = [] # the list of dicts to be returned

		for entry in feed.entries:
			# NOTE updated to use timezone string parse function
			entry_date = parser.parse(entry.published).astimezone(pytz.utc)
			
			if now - entry_date > time_range:
				continue # skip blurbs from more than 24 hrs ago

			blurb_content = {
				'title': entry.title,
				'description': entry.summary,
				'link': entry.link,
				'date': entry_date # should be a datetime.datetime object
			}
			blurb_list.append(blurb_content)

		return blurb_list
