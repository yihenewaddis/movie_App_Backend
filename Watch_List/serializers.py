from .models import Watch_list
from rest_framework.serializers import ModelSerializer
from .models import Watch_list
class Watch_list_serializer(ModelSerializer):
    class Meta:
        model = Watch_list
        fields = ['id','Movie_id','title','poster_path','description']

    def validate_Movie_id(self,value):
        user = self.context['request'].user
        qs = Watch_list.objects.filter(Movie_id = value,user = user)
        if qs.exists():
            raise Watch_list.ValidationError("this film is alredy exist")
        return value