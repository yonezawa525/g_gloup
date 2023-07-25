#from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    userNumber = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=20)
    userSta = models.CharField(max_length=2)
    userTxt = models.CharField(max_length=255)
    userUp = models.DateTimeField(null=True)
    

# Create your models here.
