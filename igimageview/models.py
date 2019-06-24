import uuid

from django.db import models

# Create your models here.
class IGPost(models.Model):
    """Model representing an Instagram post."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this instagram post')

    url = models.CharField(max_length=512, help_text='Enter IG Post URL')

    poster_name = models.CharField(max_length=512, help_text='Enter the Instagram Posters name.')

    type = ()

    def __str__(self):
        """String representation of the IG Post. Using the post's URL for now."""
        return self.url

class IGImage(models.Model):
    """Model representing an Instagram image."""
    pass
