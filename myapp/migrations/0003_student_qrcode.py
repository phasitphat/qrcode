# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-16 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qrcode',
            field=models.ImageField(blank=True, upload_to='qrcode_image'),
        ),
    ]
