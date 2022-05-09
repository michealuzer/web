from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to ='pictures')
    content_title = models.TextField()
    content_all = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

