from django.db import models
from PIL import Image # pillow for handling outlet image logo
# Create your models here.

# model for news outlets
class Outlet(models.Model):
	rss_url = models.CharField(max_length=255) # RSS url
	name = models.CharField(max_length=255) # outlet name
	logo = models.ImageField(default= 'default.png', upload_to='outlet_logos') # TODO setup media folder

	def __str__(self):
		return f'Outlet: {self.name}'

# model for blurb posts
class Blurb(models.Model):
	title = models.CharField(max_length=255) # article title
	description = models.TextField(blank=True, default="") # article description
	outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, blank=True, null=True) # news outlet poster
	link = models.CharField(max_length=255) # external url for article, I think 255 is plenty
	# upvotes = models.ManyToManyField(User, related_name='upvoted_blurbs', blank=True)
	# downvotes = models.ManyToManyField(User, related_name='downvoted_blurbs', blank=True)
	# TODO: getting upvotes/downvotes working properly requires User system, for next sprint


