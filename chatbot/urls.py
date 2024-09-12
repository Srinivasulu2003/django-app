


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatbot/chat/', views.chat, name='chat'),
]



