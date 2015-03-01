from django.db import models

from model_utils.models import TimeStampedModel

from questions.models import Question, Choice
from accounts.models import User


class Vote(TimeStampedModel):
    question = models.ForeignKey(Question, related_name="votes")
    choice = models.ForeignKey(Choice, related_name="votes")

    user = models.ForeignKey(User, related_name="votes")
    user_agent = models.CharField(max_length=255, blank=True)
    ip = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('-created',)
        unique_together = (('question', 'choice', 'user'),)

    def __unicode__(self):
        return "Vote for {}".format(self.choice)

# Possible data about each vote:
# https://developers.facebook.com/docs/graph-api/reference/v2.2/user
# https://docs.djangoproject.com/en/1.7/ref/contrib/gis/geoip/
# https://github.com/selwin/python-user-agents
