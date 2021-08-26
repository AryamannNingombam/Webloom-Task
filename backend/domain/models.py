from django.db import models
from django.contrib.auth.models import User

 
# Create your models here.


class DomainEnding(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class DomainSearched(models.Model):
    sno = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    searches = models.TextField()

    def __str__(self):
        return self.user.username
