# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(verbose_name='제목', max_length=100),
        ),
    ]
