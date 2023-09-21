from django.shortcuts import render
from .models import Comment
from rest_framework import generics,permissions,authentication
from .serializers import Comment_serializer
from .permisions import isstafpermision
class Add_list_comment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment_serializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        users = self.request.user
        serializer.save(user = users)

class list_comment(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment_serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']
        return Comment.objects.filter(movie_id=id)
class update_comment(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Comment_serializer
    permission_classes = [permissions.IsAdminUser,isstafpermision]
    
# Create your views here.
