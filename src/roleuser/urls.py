from django.urls import path

from roleuser import views

urlpatterns = [
    path('', views.index, name='index'),
]