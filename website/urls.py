from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_home'),
    path('noot', views.noot, name='index_noot'),
    path('messages', views.index_messages, name='index_messages'),
    path('messages/<str:id>', views.show_message, name='show_message')

]
