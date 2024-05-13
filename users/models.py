'''
Contributor: Alexander Aldama-Apodaca
'''

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/default.png', upload_to='pfps') # TODO check that this is the right default image path 
    articles_read = models.PositiveIntegerField(default=0)

    def has_badge(self):
        return (self.articles_read > 10)

    def __str__(self):
    	return f'{self.user.username} profile (read {self.articles_read})'

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
        super().save(*args, **kwargs)  
        # Save the model using the parent class's save method.

        img = Image.open(self.image.path)  
        # Open the image file of the profile.

        # Resize the image if either dimension is greater than 300 pixels.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  
            # Resize the image to fit within the output_size box.
            img.save(self.image.path)  
            # Save the resized image back to the same path.
