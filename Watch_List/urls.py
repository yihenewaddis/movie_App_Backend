from django.urls import path
from .views import Watch_list_view,Watch_list_delete

urlpatterns = [
    path('addCreate/', Watch_list_view.as_view()),
    path('updateDelete/<int:pk>/', Watch_list_delete.as_view()),
] 