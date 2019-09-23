from django.urls import path
from django.urls import include, path
from . import views

app_name = 'Post'
urlpatterns = [
    path('<int:post_id>/', views.OnePost.as_view(), name='onePost'),
    path('create-post/', views.CreatePost.as_view(), name='create_post'),
    path('post-created/', views.PostCreated.as_view(), name='post_created'),
]
