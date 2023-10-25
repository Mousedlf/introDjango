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

]
