from django.contrib import admin

from .models import User
from .models import Language 
from .models import Message
from .models import Proficiency

# Register your models here.

admin.site.register(User)
admin.site.register(Language)
admin.site.register(Message)
admin.site.register(Proficiency)