from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('topic/create/', views.topic_create, name='topic_create'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:topic_pk>/post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_pk>/comment/create/', views.comment_create, name='comment_create'),
    path('register/', views.register, name='register'),
]
