from django.db import models
from PIL import Image # pillow for handling outlet image logo


# model for news outlets
class Outlet(models.Model):
	rss_url = models.CharField(max_length=255) # RSS url
	name = models.CharField(max_length=255) # outlet name
	logo = models.ImageField(default= 'default.png', upload_to='outlet_logos') 

	# override save function for saving logo images at a specific size
	def save(self, *args, **kwargs):
		# (reused from similar code from project 2)
		super().save(*args, **kwargs)

		img = Image.open(self.logo.path)

		if img.height > 300 or img.width > 300: # 300x300 image thumbnail
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.logo.path)

	def __str__(self):
		return f'Outlet {self.name}'

# model for blurb posts
class Blurb(models.Model):
	title = models.CharField(max_length=255) # article title
	description = models.TextField(blank=True, default="") # article description
	outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, blank=True, null=True) # news outlet poster
	link = models.CharField(max_length=255) # external url for article, I think 255 is plenty
	date = models.DateTimeField(default=None) # date/time of publishing by the article
	# NOTE: date field is in UTC, convert to proper timezone in view

	# upvotes = models.ManyToManyField(User, related_name='upvoted_blurbs', blank=True)
	# downvotes = models.ManyToManyField(User, related_name='downvoted_blurbs', blank=True)
	# TODO: getting upvotes/downvotes working properly requires User system, for next sprint

	# TODO: look into using a custom manager (django docs say that it's "preferred")
	# https://docs.djangoproject.com/en/5.0/ref/models/instances/#creating-objects
	@classmethod
	def create(cls, blurb_content, source):
		"""creates a blurb object using a dictionary.

		Keyword arguments:
		blurb_content -- a dictionary formatted like so:
			{
				'title': title (string)
				'description': description (string)
				'link': link (string)
				'date': date (formatted datetime object)
			}
		source -- news outlet object

		Return: a new blurb object (does not save it to DB though)
		"""

		blurb = cls(
			title=blurb_content['title'],
			description=blurb_content['description'],
			link=blurb_content['link'],
			date=blurb_content['date'],
			outlet=source
		)

		return blurb

	def __str__(self):
		return f'Blurb {self.title} from {self.outlet.name}'


