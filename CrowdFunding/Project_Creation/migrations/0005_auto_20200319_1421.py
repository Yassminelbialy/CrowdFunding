# Generated by Django 3.0 on 2020-03-19 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project_Creation', '0004_auto_20200319_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Images_project', to='Project_Creation.Projects'),
        ),
    ]
