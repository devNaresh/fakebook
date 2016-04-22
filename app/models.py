from datetime import datetime

from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Posts(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()

    def __str__(self):
        return "{0}".format(self.text[:10])

    def get_commets(self):
        return self.posts_comments.all()

    def get_time(self):
        return datetime.strftime(self.modified, "%H:%M:%S %b/%d/%Y")


class Comments(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Posts, related_name="posts_comments")
    text = models.TextField()

    def __str__(self):
        return "{0}".format(self.text)

    def get_time(self):
        return datetime.strftime(self.modified, "%H:%M:%S %b/%d/%Y")
