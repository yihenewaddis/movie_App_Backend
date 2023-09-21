from .models import Comment
from rest_framework import serializers
class Comment_serializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only = True)
    is_replied = serializers.SerializerMethodField(read_only = True)
    replay = serializers.SerializerMethodField(read_only = True)
    liked = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model=Comment
        fields=['id','title','movie_id','movie_comment','replay','No_of_like','is_replied','user','liked','date_posted']
    def get_user(self,obj):
        return  obj.user.email
    def get_is_replied(self,obj):
        return f'{obj.is_replied}'
    def get_replay(self,obj):
        return f'{obj.replay}'
    
    '''in here we should be replace Favorite_List to liked comme'''
    def get_liked(self,obj):
        liked = False
        return liked
    