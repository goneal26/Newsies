# rss feed fetching, with help
# from https://stackoverflow.com/questions/70859953/how-to-update-my-django-database-with-rss-feed-every-x-minutes

import feedparser
from datetime import datetime, timedelta
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
		now = datetime.now()
		time_range = timedelta(days=1)
		feed = feedparser.parse(url)
		blurb_list = [] # the list of dicts to be returned

		for entry in feed.entries:
			entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z").astimezone(pytz.utc)

			# TODO: maybe add some better timezone formatting to keep things compatible
			# i.e. not all rss feeds represent timezone (%Z) as 'GMT', some use a UTC offset instead
			# I know this method at least works for the BBC though
			blurb_content = {
				'title': entry.title,
				'description': entry.summary,
				'link': entry.link,
				'date': entry_date # should be a datetime.datetime object
			}
			blurb_list.append(blurb_content)

		return blurb_list
