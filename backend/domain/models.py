from django.db import models
from django.contrib.auth.models import User

 
# Create your models here.

# this model would be used to give suggestions
# to the user when he/she searches for a domain;
class DomainEnding(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


# this model would be storing the history of the 
# user, keeping track of the urls that he searched for;
class DomainSearched(models.Model):
    sno = models.AutoField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    searches = models.TextField()

    def __str__(self):
        return self.user.username
