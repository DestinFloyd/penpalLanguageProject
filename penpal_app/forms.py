from django import forms 
from .models import User
from .models import Message
from .models import Language
from .models import Proficiency

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email')

class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ('toUser', 'fromUser', 'language', 'text')

class ProficiencyForm(forms.ModelForm):
    
    class Meta:
        model = Proficiency
        fields = ('level', 'user', 'language')

class LanguageForm(forms.ModelForm):
    
    class Meta:
        model = Language
        fields = ('name', 'averageProficiency')
