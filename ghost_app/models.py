from django.db import models
from django.utils import timezone

# Create your models here.
class VoteChoice(models.Model):
    choice = models.BooleanField(default=False)
    text = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.text 