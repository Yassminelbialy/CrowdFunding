# Generated by Django 3.0.4 on 2020-03-16 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
        ('Project_Creation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='project_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Project_Creation.Projects'),
        ),
        migrations.AddField(
            model_name='images',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.Users'),
        ),
        migrations.AddField(
            model_name='projects',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Project_Creation.Category'),
        ),
        migrations.AddField(
            model_name='projects',
            name='image_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Project_Creation.Images'),
        ),
        migrations.AddField(
            model_name='projects',
            name='tags_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Project_Creation.Tags'),
        ),
        migrations.AddField(
            model_name='projects',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authentication.Users'),
        ),
        migrations.AddField(
            model_name='tags',
            name='project_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Project_Creation.Projects'),
        ),
    ]
