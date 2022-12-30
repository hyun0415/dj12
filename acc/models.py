from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    comment = models.TextField(blank=True)
    point = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="user/%y") # %m %d

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/NoImage.png"