import factory

from .models import Stream


class StreamFactory(factory.DjangoModelFactory):
    title = "Don't stop believin'"
    slug = "dont-stop-belivin"

    class Meta:
        model = Stream
