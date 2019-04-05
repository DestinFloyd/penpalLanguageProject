from django.db import models
from django.db.models import Avg
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
   
    def __str__(self):
        return (self.firstName)


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    averageProficiency = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return (self.name)   
    

class Proficiency(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proficiency")
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="language")

  

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagesSent")
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagesRecieved")
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="messagesLanguage")
    text =  models.TextField()
    def __str__(self):
        return (self.text)

    # def validate_close_prof(self):



# userOne = User.objects.filter(id=fromUser).user 
# userTwo = User.objects.filter(id=toUser).user 
    #     if User.objects.filter(id=fromUser).user - self.toUser > 2:
    #         raise ValidationError(_('Sorry please pick a penpal with closer proficiency'))
    #     elif self.fromUser - self.toUser < -2:
    #         raise ValidationError(_('Sorry please pick a penpal with closer proficiency')) 
    # def save(self, *args, **kwargs):
    #     super(MyModel, self).save(*args, **kwargs)    
    # try: 
    #     validate_close_prof(self)
    # except ValidationError as e:
    #     non_field_errors = e.message_dict[NON_FIELD_ERRORS]

def check():
    actualAverage = Proficiency.objects.filter(language = id).aggregate(Avg('level'))