from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL
class Favorite_List(models.Model):
    user = models.ForeignKey(user,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=500)
    MovieId = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)

    def __str__(self):
        return self.title
# Create your models here.
