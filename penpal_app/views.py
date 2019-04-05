from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import User 
from .models import Message
from .models import Language
from .models import Proficiency

from .serializers import UserSerializer
from .serializers import LanguageSerializer
from .serializers import ProficiencySerializer
from .serializers import MessageSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ProficiencyView(viewsets.ModelViewSet):
    queryset = Proficiency.objects.all()
    serializer_class = ProficiencySerializer

class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



