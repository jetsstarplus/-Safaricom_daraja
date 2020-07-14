from django.urls import path, include
from .views import UserList, UserDetails, GroupList

urlPatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]