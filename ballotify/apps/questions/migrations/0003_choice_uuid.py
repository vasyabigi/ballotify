# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20150301_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='uuid',
            field=django_extensions.db.fields.ShortUUIDField(default='asdad', max_length=8, editable=False, blank=True),
            preserve_default=False,
        ),
    ]
