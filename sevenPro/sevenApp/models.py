from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    tuser = models.OneToOneField(User, on_delete=models.CASCADE)

    # Our extra attributess
    portfolio_site = models.URLField(blank=True)
    prof_pict = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.tuser.username

