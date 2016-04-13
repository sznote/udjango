# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0007_auto_20160413_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='ref_id',
        ),
    ]
