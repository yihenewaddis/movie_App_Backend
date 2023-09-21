from .models import Report
from rest_framework import serializers
class Report_serializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model=Report
        fields=['id','title','movie_id','user','Report_Content','Aditional_content','date_posted']
    def get_user(self,obj):
        return  obj.user.email
    
    '''in here we should be replace Favorite_List to liked comme'''
