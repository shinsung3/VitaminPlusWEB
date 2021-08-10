from django.db import models
from django.conf import settings

# Create your models here.
class ChatData(models.Model):
    index = models.IntegerField(null=True)
    liveTime = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
    memberDiff = models.CharField(max_length=200, null=True) #message, manager
    chat = models.CharField(max_length=500, null=True)
    userCode = models.IntegerField(null=True)
    userGroup = models.IntegerField(null=True)
    userId = models.CharField(max_length=200, null=True)
    userName = models.CharField(max_length=200, null=True)
    userNick = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
