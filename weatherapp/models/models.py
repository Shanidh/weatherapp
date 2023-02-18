from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.
class CustomUser(AbstractUser):
    """Model definition for User."""

    # error_messages = {"slug": {"unique": "Username Already Exists."}}

    # username=models.CharField(max_length=20)
    # password=models.CharField(max_length=20)

    # slug = models.SlugField(
    #     help_text=_("Slug of the User"),
    #     unique=True,
    #     max_length=500,
    #     error_messages=error_messages["slug"],
    #     null=True,
    # )

    # def save(self, *args, **kwargs):
    #     if self.password:
    #         self.password = make_password(self.password)
    #     super(MyUser, self).save(*args, **kwargs)

    # def __str__(self):
    #     """Unicode representation of User."""
    #     return self.username

    # def save(self, *args, **kwargs):
    #     """Save method for User."""
    #     self.slug = slugify(self.username)
    #     return super().save(*args, **kwargs)    

    pass

    