from django.db import models
from django.utils import timezone

from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from unidecode import unidecode


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        now = timezone.now()
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_active=True,
            is_staff=False,
            is_superuser=False,
            last_login=now,
            date_joined=now,
            **kwargs
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Users within the Django authentication system are represented by this model.

    email is required. Other fields are optional.

    """
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        ordering = ('email', 'name')

    def __str__(self):
        return '{name} <{email}>'.format(name=self.name, email=self.email)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(u"{}".format(self.name)))
        return super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        """
        Display user in admin interface.

        """
        return self.email
