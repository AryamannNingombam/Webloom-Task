from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class DomainEnding(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,unique=True)


    def __str__(self):
        return self.name

class DomainSearched(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    searchers = models.ManyToManyField(User)

    def __str__(self):
        return self.name



