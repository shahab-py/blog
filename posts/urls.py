from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostView.as_view(), name = 'posts'),
    path('', views.CommentView.as_view(), name = 'comments'),
]