from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
            user.set_unusable_password()

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
    name = models.CharField(max_length=255, blank=True)

    # Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Facebook
    username = models.CharField(max_length=255, unique=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        ordering = ('email', 'name')

    def __str__(self):
        return '{name} <{email}>'.format(name=self.name, email=self.email)

    def get_short_name(self):
        """
        Display user in admin interface.

        """
        return self.email
