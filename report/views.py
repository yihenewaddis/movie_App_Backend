from django.shortcuts import render
from .models import Report
from rest_framework import generics,permissions,authentication
from .serializers import Report_serializer
from .permisions import isstafpermision
class Add_Report(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = Report_serializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        users = self.request.user
        serializer.save(user = users)
class List_Report(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = Report_serializer
    permission_classes = [permissions.IsAdminUser,isstafpermision]
