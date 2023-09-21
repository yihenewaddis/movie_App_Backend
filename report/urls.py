from .views import Add_Report,List_Report
from django.urls import path
urlpatterns = [
    path('add/', Add_Report.as_view()),
    path('List/', List_Report.as_view()),
] 