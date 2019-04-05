from django.urls import path, include 
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('message', views.MessageView)
router.register('proficiency', views.ProficiencyView)
router.register('user', views.UserView)
router.register('language', views.LanguageView)



urlpatterns = [
    path('', include(router.urls))
]

