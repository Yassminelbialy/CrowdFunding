from django.db import models
# from .validators import validate_even
# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    image = models.ImageField()
    email = models.EmailField(max_length=254)
    phone=models.CharField(max_length=11)
    is_active=models.BooleanField()
    
    def __str__(self):
        return self.first_name





