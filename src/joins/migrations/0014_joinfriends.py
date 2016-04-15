# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0013_auto_20160413_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinFriends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.OneToOneField(related_name='Shared', to='joins.Join')),
                ('emailall', models.ForeignKey(related_name='emailall', to='joins.Join')),
                ('friends', models.ManyToManyField(related_name='Friend', null=True, to='joins.Join', blank=True)),
            ],
        ),
    ]
