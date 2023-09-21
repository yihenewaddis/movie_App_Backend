from django.contrib import admin
from .models import useracount

class Admin_Controler(admin.ModelAdmin):
    list_display = ['First_Name','Last_Name','email', 'Phone_No','is_staff','is_superuser']
    search_fields  = ["email",'Phone_No']
    list_filter = ['is_active','is_staff','is_superuser']
admin.site.register(useracount,Admin_Controler)
# Register your models here.
