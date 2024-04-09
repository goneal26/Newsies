# SCRATCH FILE
# for testing out RSS feed fetching

# SOURCE: https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc

import feedparser
from datetime import datetime, timedelta

now = datetime.now()
time_range = timedelta(days=1)

# testing with BBC
url = "https://feeds.bbci.co.uk/news/rss.xml"
feed = feedparser.parse(url)

# get basic stats about the feed
print(f"Feed title: {feed.feed.title}")
print(f"Feed description: {feed.feed.description}")
print(f"Feed link: {feed.feed.link}")
print("--------------------------------------------------------\n")

for entry in feed.entries:
	entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
	if now - entry_date <= time_range:
		print("Entry Title:", entry.title)
		print("Entry Link:", entry.link)
		print("Entry Published Date:", entry.published)
		print("Entry Summary:", entry.summary)
		print("\n")