from datetime import datetime

from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel


class Posts(TimeStampedModel):
    """
    Model for user Posts

     --- Methods ---

    1)  get_comments() : Return all comments on post
    2)  get_time() : Return modified time of post

    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()

    def __str__(self):
        return "{0}".format(self.text[:10])

    def get_commets(self):
        return self.posts_comments.all()

    def get_time(self):
        return datetime.strftime(self.modified, "%H:%M:%S %b/%d/%Y")


class Comments(TimeStampedModel):
    """
    Model for Comments on Posts

     --- Methods ---

    1)  get_time() : Return modified time of post

    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Posts, related_name="posts_comments")
    text = models.TextField()

    def __str__(self):
        return "{0}".format(self.text)

    def get_time(self):
        return datetime.strftime(self.modified, "%H:%M:%S %b/%d/%Y")
