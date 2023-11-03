from django.urls import path

from . import views

urlpatterns = [
    path('messages', views.get_messages),
    path('message/new', views.new_message),
    path('message/<str:id>', views.get_message),
    path('message/edit/<str:id>', views.edit_message),
    path('message/delete/<str:id>', views.delete_message),
    path('register', views.register_user),
]