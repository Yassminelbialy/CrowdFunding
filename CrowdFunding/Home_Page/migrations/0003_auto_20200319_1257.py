# Generated by Django 3.0.4 on 2020-03-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0002_auto_20200316_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate_value',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]
