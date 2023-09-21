from django.db import models
from django.conf import settings
user = settings.AUTH_USER_MODEL
class Report(models.Model):
    user = models.ForeignKey(user,null=True,on_delete=models.CASCADE)
    title = models.TextField()
    movie_id = models.CharField(max_length=500)
    Report_Content= models.TextField()
    Aditional_content= models.TextField()
    Is_Resolved=models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['date_posted']
