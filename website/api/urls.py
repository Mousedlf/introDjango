from django.urls import path

from . import views

urlpatterns = [
    path('messages', views.get_messages),
    path('message/new', views.new_message),
    path('message/<str:id>', views.get_message),
]