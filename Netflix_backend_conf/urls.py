from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from .view import RefreshTokenView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('favorite/', include('Favorite_List.urls')),
    path('comment/', include('comment.urls')),
    path('watchlater/', include('Watch_List.urls')),
    path('report/', include('report.urls')),
    path('auth/token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]
urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name = 'index.html'))] 