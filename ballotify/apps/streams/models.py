from django.db import models
from django.template.defaultfilters import slugify

from model_utils.models import TimeStampedModel
from unidecode import unidecode

from accounts.models import User


class StreamQuerySet(models.QuerySet):
    def public(self):
        return self.filter(is_default=False)

    def get_default(self):
        return self.filter(is_default=False).first()


class Stream(TimeStampedModel):
    owner = models.ForeignKey(User, related_name="owned_streams")
    is_default = models.BooleanField(default=False)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    followers = models.ManyToManyField(User, related_name="followed_streams", through='StreamMembership')

    objects = StreamQuerySet.as_manager()

    class Meta:
        unique_together = (('owner', 'title'), ('owner', 'slug'))
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(u"{}".format(self.title)))

        return super(Stream, self).save(*args, **kwargs)


class StreamMembership(TimeStampedModel):
    stream = models.ForeignKey(Stream)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (('stream', 'user'), )
        ordering = ('-created',)

    def __unicode__(self):
        return "{} - {}".format(self.stream, self.user)
