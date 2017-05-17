# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 00:09
from __future__ import unicode_literals

import accounts.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_password', models.CharField(max_length=128, verbose_name='user_password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('user_role', models.CharField(choices=[('RoleA', 'RoleA'), ('RoleB', 'RoleB')], default='RoleA', max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'tbl_users',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
    ]
