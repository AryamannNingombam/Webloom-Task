from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
# this model is there to check if the user
# has verified his account or not, if not, he cannot log in
# . an email is sent to him to verify his account 
class UserVerified(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    verified = models.BooleanField(default=False, null=False)
    verification_id = models.CharField(max_length=100,default="XXXX")

    def __str__(self):
        return self.user.username
