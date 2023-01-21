from django.urls import path

from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login_user"),
    path('chat', views.chatbot, name="chatbot"),
]
