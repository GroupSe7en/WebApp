from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from PIL import Image


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
        if (self.groups.filter(name='Lecturer').exists()):
            return self.lecturerprofile.firstName + " " + self.lecturerprofile.lastName
        elif (self.groups.filter(name='Student').exists()):
            return self.studentprofile.firstName + " " + self.studentprofile.lastName
        else:
            return ""

class Profile(models.Model):
    
    firstName = models.CharField(max_length=50, verbose_name="First Name")
    lastName = models.CharField(max_length=50, verbose_name="Last Name")
   
    image = models.ImageField(default='defaultDP.jpg', upload_to='profile_pics', verbose_name="Profile Picture")

    def __str__(self):
        return f'{self.user.email} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        abstract = True

class StudentProfile(Profile):
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

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="studentprofile")
    indexNo = models.CharField(max_length=7, verbose_name="Index Number")
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES, verbose_name="Department")
    contactNo = models.CharField(max_length=10, verbose_name="Contact Number")

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

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="lecturerprofile")
    department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES, verbose_name="Department")