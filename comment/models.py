from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL
class Comment(models.Model):
    user = models.ForeignKey(user,null=True,on_delete=models.CASCADE)
    title = models.TextField()
    movie_id = models.CharField(max_length=500)
    movie_comment = models.TextField()
    replay = models.TextField(null=True)
    No_of_like = models.IntegerField(default=0)
    is_replied = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['date_posted']
    