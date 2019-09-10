from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.OnePost.as_view(), name='onePost'),
]
