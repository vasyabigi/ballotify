import factory

from .models import User

USER_PASSWORD = "2fast2furious"


class UserFactory(factory.DjangoModelFactory):
    name = "John Doe"
    username = "pedro"
    email = factory.Sequence(lambda n: "john{}@example.com".format(n))
    password = factory.PostGenerationMethodCall('set_password', USER_PASSWORD)
    gender = "male"

    class Meta:
        model = User
