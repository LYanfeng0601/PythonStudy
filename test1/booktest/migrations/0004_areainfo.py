# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_auto_20190902_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('atitle', models.CharField(max_length=20)),
                ('aparent', models.ForeignKey(to='booktest.AreaInfo', null=True, blank=True)),
            ],
        ),
    ]
