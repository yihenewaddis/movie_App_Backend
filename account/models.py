from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
class userAcountManager(BaseUserManager):
    def create_user(self,email,First_Name,Last_Name, Phone_No,password=None):
        if not email:
            raise ValueError('user mest have an email address') 
        email = self.normalize_email(email)
        user = self.model(email=email,First_Name=First_Name,Last_Name=Last_Name,Phone_No=Phone_No)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,First_Name,Last_Name,Phone_No, password=None):
        if not email:
            raise ValueError('user mest have an email address') 
        email = self.normalize_email(email)
        user = self.model(email=email,First_Name=First_Name,Last_Name=Last_Name,Phone_No=Phone_No)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class useracount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Phone_No = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    objects = userAcountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['First_Name','Last_Name','Phone_No']

    def __str__(self):
        Full_name = self.First_Name+' '+self.Last_Name 
        return Full_name
