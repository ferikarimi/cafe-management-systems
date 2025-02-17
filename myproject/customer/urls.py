from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    profile,
    view_messages,
    send_message,
    
)

urlpatterns = [
    path('api/register/', register, name='register'),
    path('api/login/', user_login, name='login'),
    path('api/logout/', user_logout, name='logout'),
    path('api/profile/', profile, name='profile'),
    path('api/messages/', send_message, name='send_message'),
     path('api/view-messages/', view_messages, name='view_messages'),
]