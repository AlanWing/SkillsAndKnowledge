# Generated by Django 3.1.1 on 2020-09-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_management', '0009_auto_20200922_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='access',
            name='district',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
