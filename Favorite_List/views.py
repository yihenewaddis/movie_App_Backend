from django.shortcuts import render
from .models import Favorite_List
from rest_framework import generics,permissions,authentication
from .serializers import Favorite_List_Serializer
class Add_To_Favorite(generics.ListCreateAPIView):
    queryset = Favorite_List.objects.all()
    serializer_class = Favorite_List_Serializer
    permission_classes = [permissions.IsAuthenticated]
    '''
    all authenticated user can add and retrive favorite list contents
    '''
    def perform_create(self, serializer):
        users =  self.request.user
        serializer.save(user = users)
    def get_queryset(self):
        qs =  super().get_queryset()
        user = self.request.user
        return qs.filter(user = user)

class Update_Delete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite_List.objects.all()
    serializer_class = Favorite_List_Serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs =  super().get_queryset()
        user = self.request.user
        return qs.filter(user = user)

