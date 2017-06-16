# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='permission_group',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='user',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='user_group',
            name='basemodel_ptr',
        ),
        migrations.RemoveField(
            model_name='user_permission',
            name='basemodel_ptr',
        ),
        migrations.DeleteModel(
            name='BaseModel',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Permission_Group',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User_Group',
        ),
        migrations.DeleteModel(
            name='User_Permission',
        ),
    ]
