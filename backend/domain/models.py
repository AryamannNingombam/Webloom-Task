from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DomainSearched(models.Model):
    name = models.CharField(max_length=50, unique=True)
    searchers = models.ManyToManyField(User)
