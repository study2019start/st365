from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    loginname = models.TextField(max_length=50)
    password = models.TextField(max_length=50)
    #updatetime = models.DateTimeField()
    #lastchapter = models.CharField(max_length=100)

class user_info(models.Model):
    name = models.TextField(max_length=50)
    tel = models.IntegerField(null=True)
    cer = models.IntegerField(null=True)
    uid = models.OneToOneField(user,on_delete=models.CASCADE)

def __str__(self):
    return self.text