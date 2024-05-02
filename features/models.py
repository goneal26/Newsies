from django.db import models
from PIL import Image # pillow for handling outlet image logo
from django.contrib.auth.models import User
from django.urls import reverse

# model for news outlets
class Outlet(models.Model):
	rss_url = models.CharField(max_length=255) # RSS url
	page_url = models.CharField(max_length=255, default="")
	name = models.CharField(max_length=255) # outlet name
	logo = models.ImageField(default='images/default.png', upload_to='outlet_logos') 
	followers = models.ManyToManyField(User, blank=True)
	# ^ manytomany should be right?

	# override save function for saving logo images at a specific size
	def save(self, *args, **kwargs):
		"""
        Overrides the default save method to add custom logic for processing the
         image field.

        If the image's height or width exceeds 300 pixels, it resizes the image 
        to fit within a 300x300 box while maintaining aspect ratio.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
		# (reused from similar code from project 2)
		super().save(*args, **kwargs)

		img = Image.open(self.logo.path)

		if img.height > 300 or img.width > 300: # 300x300 image thumbnail
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.logo.path)

  # def get_absolute_url(self): # url for a specific outlet
  # 	return reverse('outlets:outlet', kwargs={'pk': self.pk})

	def __str__(self):
		return f'Outlet {self.name}'


# model for blurb posts
class Blurb(models.Model):
	title = models.CharField(max_length=255) # article title
	description = models.TextField(blank=True, default="") # article description
	outlet = models.ForeignKey(
		Outlet, 
		on_delete=models.CASCADE,
		blank=True,
		null=True
	) # news outlet that "posted" the blurb (i.e. where it was fetched from)

	link = models.CharField(max_length=255) 
	# external url for article, I think 255 is plenty

	date = models.DateTimeField(default=None)
	# date/time of publishing by the article
	# NOTE: date field is in UTC, convert to proper timezone in view

	# upvotes and downvotes, relate to users
	upvotes = models.ManyToManyField(
		User, 
		related_name='upvoted_blurbs', # TODO: look into related name docs 
		blank=True
	)
	downvotes = models.ManyToManyField(
		User, 
		related_name='downvoted_blurbs', 
		blank=True
	)
	

	# TODO: look into using a custom manager (django docs say it's "preferred")
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

	#def get_absolute_url(self): # url for a specific blurb
	#return reverse('blurbs:blurb', kwargs={'pk': self.pk})
	# TODO add abs urls to urls.py

	def __str__(self):
		return f'Blurb {self.title} from {self.outlet.name}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    photo = models.ImageField(upload_to='posts/')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
