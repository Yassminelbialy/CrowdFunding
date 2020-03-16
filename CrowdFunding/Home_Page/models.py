from django.db import models
from Authentication.models import Users
from  Project_Creation.models import Projects

class Rate(models.Model):
    id=models.AutoField(primary_key=True)
    rate_value=models.DecimalField(max_digits=11, decimal_places=11)
    ## FK
    user_id=models.ForeignKey(Users, on_delete = models.CASCADE,null=True)
    project_Id=models.ForeignKey(Projects, on_delete = models.CASCADE,null=True)
    def __str__(self):
            return self.rate_value

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    content=models.TextField()
    ## FK
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    project_Id=models.ForeignKey(Projects, on_delete = models.CASCADE,null=True)
    def __str__(self):
            return self.content

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.CharField(max_length=100, null=True)
     ## FK
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE,null=True)
    project_Id=models.ForeignKey(Projects, on_delete = models.CASCADE,null=True)
    def __str__(self):
            return self.note
