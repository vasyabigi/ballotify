from django.db import models
from django.template.defaultfilters import slugify

from model_utils.models import TimeStampedModel
from unidecode import unidecode

from accounts.models import User


class Stream(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    user = models.ForeignKey(User, related_name="streams")
    followers = models.ManyToManyField(User, related_name="followed_streams")

    class Meta:
        unique_together = (('user', 'title'), ('user', 'slug'))
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(u"{}".format(self.title)))

        return super(Stream, self).save(*args, **kwargs)
