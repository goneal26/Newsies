from django.db import models
from PIL import Image # pillow for handling outlet image logo
from django.contrib.auth.models import User
from django.urls import reverse

# model for tags! (super simple)
# @Tre-ONeal
class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True) # okay max length for tags for now

	def __str__(self):
		return f'#{self.name}'

# model for news outlets
# @Tre-ONeal
class Outlet(models.Model):
	rss_url = models.CharField(max_length=255) # RSS url
	page_url = models.CharField(max_length=255, default="")
	name = models.CharField(max_length=255) # outlet name
	logo = models.ImageField(default='images/default.png', upload_to='outlet_logos') 
	followers = models.ManyToManyField(User, blank=True)

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
# @Tre-ONeal
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
	# NOTE may need to increase max length later

	date = models.DateTimeField(default=None)
	# date/time of publishing by the article
	# NOTE: date field is in UTC by default, may need to change

	# upvotes and downvotes, relate to users
	upvotes = models.ManyToManyField(
		User, 
		related_name='upvoted_blurbs',
		blank=True
	)
	downvotes = models.ManyToManyField(
		User, 
		related_name='downvoted_blurbs', 
		blank=True
	)

	# tags
	tags = models.ManyToManyField(Tag, blank=True)

	# IFTIME: look into using a custom manager (django docs say it's "preferred")
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

# model for user comments under blurbs
class Comment(models.Model):
	# user that posted the comment
	author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

	# the blurb the comment is under
	blurb = models.ForeignKey(Blurb, related_name='comments', on_delete=models.CASCADE)

	# comment text content (NOTE: parse to get tags later)
	text = models.TextField(blank=True, default="")
	
	# comment upvotes and downvotes
	# @Tre-ONeal
	upvotes = models.ManyToManyField(
		User, 
		blank=True,
		related_name = "comment_upvotes",
	)
	downvotes = models.ManyToManyField(
		User, 
		blank=True,
		related_name = "comment_downvotes"
	)

	def net_votes(self):
		return self.upvotes.count() - self.downvotes.count()

	def __str__(self):
		return f'Comment from {self.author.username} on blurb {self.blurb}'

# model for podcasts
# (not super necessary but this way we can easily add more thru admin)
# @Tre-ONeal
class Podcast(models.Model):
	url = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	logo = models.ImageField(default=None, upload_to='podcast_logos')

	def __str__(self):
		return f'Podcast {self.name}'