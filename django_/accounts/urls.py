from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/list/', UserListView.as_view()),
    path('users/<int:pk>/', UserRetrieveView.as_view()),
    path('users/<int:pk>/', UserDeleteView.as_view()),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.social.urls')),
]