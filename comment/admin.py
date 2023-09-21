from django.contrib import admin
from .models import Comment

class comment_custome(admin.ModelAdmin):
    list_display = ['title', 'movie_id','is_replied','date_posted']
    search_fields  = ["title","movie_id"]
    list_filter = ['is_replied']

admin.site.register(Comment,comment_custome)
# Register your models here.
