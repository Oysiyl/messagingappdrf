from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageList.as_view()),
    path('messages/<int:pk>/', views.MessageDetail.as_view()),
    path('messages_by_user/', views.MessageViewSpecificUserSet.as_view({'get': 'list'})),
    path('read_message/<int:pk>/', views.ReadMessageSet.as_view({'get': 'retrieve'}))
]
