# SCRATCH FILE
# for testing out RSS feed fetching

# SOURCE: https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc
# I've modified things significantly from the source, this is just a scratch file for testing feed fetching
# (specifically if our timezone parsing works)

import feedparser
from datetime import datetime, timedelta
from dateutil import parser
import pytz

now = datetime.now().astimezone(pytz.utc)
time_range = timedelta(days=1)

url = input("Enter feed url: ")
feed = feedparser.parse(url)

# get basic stats about the feed
print(f"Feed title: {feed.feed.title}")
print(f"Feed description: {feed.feed.description}")
print(f"Feed link: {feed.feed.link}")
print("--------------------------------------------------------\n")

for entry in feed.entries:
	entry_date = parser.parse(entry.published).astimezone(pytz.utc)
	if now - entry_date <= time_range:
		print("Entry Title:", entry.title)
		print("Entry Link:", entry.link)
		print("Entry Published Date:", entry.published)
		print("Entry Summary:", entry.summary)
		print("\n")