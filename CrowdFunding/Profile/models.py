from django.db import models
from Authentication.models import Users
from  Project_Creation.models import Projects

# Create your models here.


class ExtraInfo (models.Model):
    id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100,null=True)
    Birth_day=models.DateField(auto_now=False, auto_now_add=False,null=True)
    FB_link=models.CharField(max_length=255,null=True)
    ##FK
    User_id=models.ForeignKey(Users, on_delete = models.CASCADE,null=True)
    def __str__(self):
        return self.id


