# Generated by Django 3.2.9 on 2021-11-15 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
