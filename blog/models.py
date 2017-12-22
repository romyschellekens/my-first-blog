from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Blog(models.Model):
    user_id=models.BigIntegerField()
    user_screen_name=models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        ordering= ['-created_at']

        def __str__(self):
            return self.text
