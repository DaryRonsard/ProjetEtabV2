from django.urls import path

from absence import views

urlpatterns = [
    path('', views.index, name='index'),
]