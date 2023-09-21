from django.shortcuts import render
from .models import Watch_list
from rest_framework import generics,permissions,authentication
from .serializers import Watch_list_serializer

class Watch_list_view(generics.ListCreateAPIView):
    queryset = Watch_list.objects.all()
    serializer_class = Watch_list_serializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user = user)

class Watch_list_delete(generics.DestroyAPIView):
    queryset = Watch_list.objects.all()
    serializer_class = Watch_list_serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(user = user)