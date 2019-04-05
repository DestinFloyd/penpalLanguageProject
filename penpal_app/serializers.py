from rest_framework import serializers 
from .models import User
from .models import Message
from .models import Language
from .models import Proficiency

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('fromUser', 'toUser', 'language', 'text')

class ProficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proficiency
        fields = ('level', 'user', 'language')

class UserSerializer(serializers.ModelSerializer):
    messagesSent = MessageSerializer(many=True, read_only=True)
    messagesRecieved = MessageSerializer(many=True, read_only=True)
    proficiency = ProficiencySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'messagesSent', 'messagesRecieved', 'proficiency')

class LanguageSerializer(serializers.ModelSerializer):
    language = ProficiencySerializer(many=True, read_only=True)
    class Meta:
        model = Language
        fields = ('name', 'averageProficiency', 'language')

