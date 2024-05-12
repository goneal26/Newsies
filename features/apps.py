from django.apps import AppConfig
from django.utils import timezone

class FeaturesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'features'

    # @Tre-ONeal
    def ready(self): # added for RSS feed scheduling
        import os
        from . import jobs
    
        # RUN_MAIN check to avoid running the code twice since manage.py runserver runs 'ready' twice on startup
        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start()
            print("Starting all jobs...")
            print("Server time: ", timezone.now())

