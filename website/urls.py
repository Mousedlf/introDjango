from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_home'),
    path('noot', views.noot, name='index_noot'),
    path('messages', views.index_messages, name='index_messages'),
    path('messages/new', views.create_message, name='create_message'),
    path('messages/<str:id>', views.show_message, name='show_message'),
    path('messages/delete/<str:id>', views.delete_message, name='delete_message'),
    path('messages/edit/<str:id>', views.edit_message, name='edit_message'),
    path('messages/<str:id>/response', views.add_response, name='add_response'),
    path('messages/response/delete/<str:id>', views.delete_response, name='delete_response'),
    path('messages/response/edit/<str:id>', views.edit_response, name='edit_response'),
    path('register', views.register_user, name='register_user'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

]
