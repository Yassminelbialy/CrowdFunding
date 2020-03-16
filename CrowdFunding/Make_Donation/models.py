from django.db import models
from Authentication.models import Users
from  Project_Creation.models import Projects
# Create your models here.
class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.BigIntegerField()
     # FK
    user_id=models.ForeignKey('Authentication.Users', on_delete = models.CASCADE,null=True)
    project_Id=models.ForeignKey('Project_Creation.Projects', on_delete = models.CASCADE,null=True)
    def __str__(self):
            return self.amount