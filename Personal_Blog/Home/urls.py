from django.urls import path
from django.urls import include, path
from . import views

app_name = 'Home'
urlpatterns = [
    # Funtion view
    # path('', views.index, name='index'),
    # Class-based Views
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path(
        'add-subscriber/',
        views.AddSubscriber.as_view(),
        name='add_subscriber'
    ),
]
