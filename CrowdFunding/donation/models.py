from django.db import models
from  users import Users
from  projects import Projects
# Create your models here.
class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.BigIntegerField()
    ## FK
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    project_Id = models.ForeignKey('Projects', on_delete=models.CASCADE)
    def __str__(self):
            return self.amount
