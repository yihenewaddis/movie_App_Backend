from django.urls import path
from .views import Add_To_Favorite,Update_Delete

urlpatterns = [
    path('addCreate/', Add_To_Favorite.as_view() ),
    path('updateDelete/<int:pk>/', Update_Delete.as_view()),
] 