# for scheduling the RSS fetcher
# @Tre-ONeal
from apscheduler.schedulers.background import BackgroundScheduler
from .rss import RSSFetcher
from pytz import timezone
from datetime import datetime

# help from https://apscheduler.readthedocs.io/en/3.x/userguide.html#code-examples
def start(): 
	scheduler = BackgroundScheduler()
	scheduler.add_job(RSSFetcher.update_db, 'cron', hour=19, minute=30) # executes every day at 7:30PM
	# (weird time, but made testing easier since it wasn't midnight)
	scheduler.start()
	print("Starting RSS fetcher background scheduler job...")
	# starts a scheduler to run the RSS fetching stuff once per certain time of day (hence the arg 'cron')