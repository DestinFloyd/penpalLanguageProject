from django.urls import path
from . import views



urlpatterns = [
    path('user/', views.user_index, name='user_index'),
    path('user/new', views.user_create, name='user_create'),
    path('user/<int:id>', views.user_show, name='user_show'),
    path('user/<int:id>/edit', views.user_edit, name='user_edit'),  
    path('user/<int:id>/update', views.user_update, name='user_update'),  
    path('user/<int:id>/delete', views.user_delete, name='user_delete'), 

]
