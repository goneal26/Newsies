# for scheduling the RSS fetcher
from apscheduler.schedulers.background import BackgroundScheduler
from .rss import RSSFetcher
from pytz import timezone
from datetime import datetime

# help from https://apscheduler.readthedocs.io/en/3.x/userguide.html#code-examples
def start(): 
	scheduler = BackgroundScheduler()
	scheduler.add_job(RSSFetcher.update_db, 'cron', hour=7) # executes every day at 7AM EDT
	scheduler.start()
	# starts a scheduler to run the RSS fetching stuff once per certain time of day (hence the arg 'cron')