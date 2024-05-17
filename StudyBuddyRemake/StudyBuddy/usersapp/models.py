from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class ReceivedCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.code