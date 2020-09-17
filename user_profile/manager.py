from django.contrib.auth.models import BaseUserManager

from common_utils.constants import *




class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self,password, email=None, **extra_fields):
        """Create and save a User with the given email and password."""
       
        
        if email!=None:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        else:
            raise ValueError(EMAIL_REQUIRED)


    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email,password=password, **extra_fields)

    def create_superuser(self,password, email, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)



        if extra_fields.get('is_staff') is not True:
            raise ValueError(NEEDED_IS_STAFF)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(NEEDED_IS_SUPERUSER)

        return self._create_user(email=email, password=password, **extra_fields)

