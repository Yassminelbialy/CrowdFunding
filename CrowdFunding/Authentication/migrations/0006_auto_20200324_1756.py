# Generated by Django 3.0.4 on 2020-03-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0005_auto_20200324_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
