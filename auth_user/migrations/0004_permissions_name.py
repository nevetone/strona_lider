# Generated by Django 3.0.6 on 2020-05-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_remove_permissions_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissions',
            name='name',
            field=models.CharField(default='user', max_length=50),
        ),
    ]
