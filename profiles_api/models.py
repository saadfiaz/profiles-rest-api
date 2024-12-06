from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for userprofiles"""

    def Create_user(self, email, name, password=None):
        """Create a new profile"""
        if not email:
            raise ValueError('User Must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new supreruser with the give details"""
        user = self._create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user





class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the System"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDs = ['name']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrive Short Name of the user"""
        return self.name

    def __str__(self):
        """return String Representation of the user"""
        return self.email
