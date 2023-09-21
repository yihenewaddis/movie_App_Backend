from django.urls import path
from .views import Add_list_comment,update_comment,list_comment

urlpatterns = [
    path('addCreate/', Add_list_comment.as_view()),
    path('list/<int:id>/', list_comment.as_view()),
    path('updatedelete/<int:pk>/', update_comment.as_view()),
] 