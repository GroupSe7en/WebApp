from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):

    DEPARTMENT_CHOICES = [
    ('EN', 'ENTC'),
    ('CS', 'CSE'),
    ('BM', 'BM'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('CH', 'CH'),
    ('EE', 'EE'),
    ('CE', 'CE')
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    image = models.ImageField(default='defaultDP.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.email} Profile'

    class Meta:
        abstract = True

class StudentProfile(Profile):
    indexNo = models.CharField(max_length=7)
    contactNo = models.CharField(max_length=10)

class LecturerProfile(Profile):
    DEPARTMENT_CHOICES = [
    ('EN', 'ENTC'),
    ('CS', 'CSE'),
    ('BM', 'BM'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('CH', 'CH'),
    ('EE', 'EE'),
    ('CE', 'CE'),
    ('MA', 'MA')
    ]

    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)