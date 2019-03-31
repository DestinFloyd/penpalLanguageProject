from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=255)

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    averageProficiency = models.IntegerField(default=0)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagesSent")
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messagesRecieved")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="messagesLanguage")
    text =  models.TextField()

class Proficiency(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))), unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="language")



