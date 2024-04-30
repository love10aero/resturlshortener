# Create your models here.
import uuid
from django.db import models

def generate_uuid():
    """
    Generates a random UUID and returns the first 8 characters of it as a string.

    Returns:
        str: The first 8 characters of the generated UUID.
    """
    return str(uuid.uuid4())[:8]  # Generates an 8-character UUID.

class ShortURL(models.Model):
    url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=8, unique=True, default=generate_uuid)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.url)
