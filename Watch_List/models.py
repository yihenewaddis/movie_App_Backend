from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL

class Watch_list(models.Model):
    user = models.ForeignKey(user,null=True,on_delete=models.CASCADE)
    Movie_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_path = models.CharField(max_length=255)
# Create your models here.
