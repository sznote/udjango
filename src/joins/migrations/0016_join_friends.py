# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0015_auto_20160414_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friends',
            field=models.ForeignKey(related_name='refferral', blank=True, to='joins.Join', null=True),
        ),
    ]
