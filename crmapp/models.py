from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class App(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=225)
    price=models.IntegerField(null=True,default=0)
    image = models.ImageField(upload_to='image/',null=True) 

class Archive(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    app=models.ForeignKey(App,on_delete=models.CASCADE,null=True)