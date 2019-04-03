from django.urls import path
from . import views



urlpatterns = [
    path('user/', views.user_index, name='user_index'),
    path('user/<int:id>', views.user_show, name='user_show'),
    path('user/new', views.user_create, name='user_create'),
]