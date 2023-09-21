from django.contrib import admin
from .models import Report

class Report_custome(admin.ModelAdmin):
    list_display = ['title', 'movie_id','movie_id','Report_Content','Is_Resolved']
    search_fields  = ["title","Report_Content"]
    list_filter = ['Is_Resolved']

admin.site.register(Report,Report_custome)