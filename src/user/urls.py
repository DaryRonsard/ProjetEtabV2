from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.register_user, name='register'),
]
