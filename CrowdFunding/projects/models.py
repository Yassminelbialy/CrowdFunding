# from django.db import models
# from users.models import Users
#
# # Create your models here.
# class Projects(models.Model):
#     id=models.AutoField(primary_key=True)
#     project_name=models.CharField(max_length=100)
#     title=models.CharField(max_length=100)
#     details=models.TextField()
#     start_date=models.DateField(auto_now=False, auto_now_add=False)
#     end_date=models.DateField(auto_now=False, auto_now_add=False)
#     average_rate=models.DecimalField(max_digits=None, decimal_places=None,null=True)
#     max_target=models.BigIntegerField()
#     ##FK
#     user_id=models.ForeignKey('Users', on_delete = models.CASCADE)
#     image_id=models.ForeignKey('Images', on_delete = models.CASCADE)
#     category_id=models.ForeignKey('Category', on_delete = models.CASCADE)
#     tags_id=models.ForeignKey('Tags', on_delete = models.CASCADE)
#     def __str__(self):
#             return self.project_name
#
#
# class Rate(models.Model):
#     id=models.AutoField(primary_key=True)
#     rate_value=models.DecimalField(max_digits=None, decimal_places=None)
#     ## FK
#     user_id=models.ForeignKey('Users', on_delete = models.CASCADE)
#     project_Id=models.ForeignKey('Projects', on_delete = models.CASCADE)
#     def __str__(self):
#             return self.rate_value
#
#
#
# class Comments(models.Model):
#     id = models.AutoField(primary_key=True)
#     content=models.TextField()
#     ## FK
#     user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
#     project_Id = models.ForeignKey('Projects', on_delete=models.CASCADE)
#     def __str__(self):
#             return self.content
#
# class Images(models.Model):
#     id = models.AutoField(primary_key=True)
#     image = models.ImageField(null=True)
#     ## FK
#     user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
#     project_Id = models.ForeignKey('Projects', on_delete=models.CASCADE)
#     def __str__(self):
#             return self.id
#
#
# class Tags(models.Model):
#     id = models.AutoField(primary_key=True)
#     tag_name = models.CharField(max_length=100)
#     ## FK
#     project_Id = models.ForeignKey('Projects', on_delete=models.CASCADE)
#     def __str__(self):
#             return self.tag_name
#
# class Report(models.Model):
#     id = models.AutoField(primary_key=True)
#     note = models.CharField(max_length=100, null=True)
#     ## FK
#     user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
#     comment_id = models.ForeignKey('Comments', on_delete=models.CASCADE)
#     project_Id = models.ForeignKey('Projects', on_delete=models.CASCADE)
#     def __str__(self):
#             return self.note
#
#
# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     def __str__(self):
#             return self.name
