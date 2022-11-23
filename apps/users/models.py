from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models import ImageField, CharField


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, username, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not username:
            raise ValueError('User must have an username.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create and return a new superuser."""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=True)
    photo = ImageField(default='media/users/user.png', blank=True, null=True)
    address = CharField(max_length=255)
    phone = CharField(max_length=25)

    objects = UserManager()
    USERNAME_FIELD = 'username'
