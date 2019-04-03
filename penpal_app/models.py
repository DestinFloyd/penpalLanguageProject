from django.db import models
from django.db.models import Avg

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
    
    # averageProficiency = Proficiency.objects.filter(language=id).aggregate(Avg('level')).values()[0]

class Proficiency(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="language")
    

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagesSent")
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagesRecieved")
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name="messagesLanguage")
    text =  models.TextField()
    def __str__(self):
        return (self.text)

    def save(self, *args, **kwargs):
        if self.fromUser 
        # its not the same lang with same level w/in2
        # https://docs.djangoproject.com/en/2.2/topics/db/models/#field-name-restrictions
            return # Not a vaild message due to language!
# forms validation 
# https://docs.djangoproject.com/en/2.1/ref/forms/validation/
# validation example clear !!
# http://www.learningaboutelectronics.com/Articles/How-to-create-a-custom-field-validator-in-Django.php
# overlap?
# Key lookups?

        else:
            super().save(*args, **kwargs)  


