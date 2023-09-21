from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
'''
The UserCreateSerializer in Djoser typically inherits from djoser.serializers.UserCreateSerializer. It extends the functionality of Django's default user creation serializer by adding additional fields and validation specific to Djoser.
'''
user = get_user_model()
''' 
the get_user_model function is a convenient way to retrieve the user model that is currently active in the Django project
'''
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = user
        fields = '__all__'
