# Generated by Django 3.2.6 on 2021-11-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_username_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='money',
            field=models.IntegerField(blank=True, default=100),
        ),
    ]
