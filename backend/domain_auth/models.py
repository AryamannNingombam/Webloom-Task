from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 

class UserVerified(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    verified = models.BooleanField(default=False, null=False)
    verification_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
