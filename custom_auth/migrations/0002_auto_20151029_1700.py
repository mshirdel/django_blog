# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='comment',
            field=models.TextField(verbose_name=b'\xd9\x85\xd8\xaa\xd9\x86 \xd9\xbe\xdb\x8c\xd8\xa7\xd9\x85'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'\xd8\xa7\xdb\x8c\xd9\x85\xdb\x8c\xd9\x84'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 10, 29, 17, 0, 51, 33775, tzinfo=utc), max_length=200, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85', blank=True),
            preserve_default=False,
        ),
    ]
