from django.db import models
from Authentication.models import Users
# from Home_Page.models import Images
# # Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
            return self.name

class Projects(models.Model):
    id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    details=models.TextField()
    start_date= models.DateField(auto_now=False, auto_now_add=False)
    end_date= models.DateField(auto_now=False, auto_now_add=False)
    average_rate=models.DecimalField(max_digits=5, decimal_places=5,null=True)
    max_target=models.BigIntegerField()
    cover=models.ImageField(null=True)
    choosen_byAdmin=models.BooleanField(default=False)
    ##FK
    user_id=models.ForeignKey(Users, on_delete = models.CASCADE,null=True)
    category_id=models.ForeignKey(Category, on_delete = models.CASCADE,null=True)

    def __str__(self):
            return self.project_name

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True)
    ## FK
    project_Id=models.ForeignKey(Projects, on_delete = models.CASCADE,null=True)
    def __str__(self):
            return self.id

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    ## FK
    project_Id=models.ForeignKey(Projects, on_delete = models.CASCADE,null=True)
    def __str__(self):
            return self.tag_name


