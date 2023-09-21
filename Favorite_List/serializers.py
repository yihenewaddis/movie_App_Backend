from .models import Favorite_List 
from rest_framework import serializers

class Favorite_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_List
        fields =["id",'title','MovieId','poster_path','backdrop_path']

    def validate_MovieId(self,value):
        user = self.context['request'].user
        qs = Favorite_List.objects.filter(MovieId = value,user = user)
        if qs.exists():
            raise serializers.ValidationError("this film is alredy exist")
        return value
