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
    path('admin/register/', register, name='register'),
    path('admin/login/', user_login, name='login'),
    path('admin/logout/', user_logout, name='logout'),
    path('admin/profile/', profile, name='profile'),
    path('admin/messages/', send_message, name='send_message'),
     path('admin/view-messages/', view_messages, name='view_messages'),
]