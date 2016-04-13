# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0009_join_ref_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='ref_id',
        ),
    ]
