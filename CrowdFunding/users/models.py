from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    password=models.BigIntegerField()
    image = models.ImageField(null=True)
    email = models.EmailField(max_length=254)
    active=models.BooleanField(defualt=False)
    phone=models.BigIntegerField()
    def __str__(self):
        return self.First_name

class ExtraInfo (models.Model):
    id=models.AutoField(primary_key=True)
    country=models.CharField(max_length=100)
    Birth_day=models.DateField(auto_now=False, auto_now_add=False)
    FB_link=models.CharField(max_length=255)
    User_id=models.ForeignKey('Users', on_delete = models.CASCADE)



