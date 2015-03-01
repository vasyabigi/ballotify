# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20150301_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='uuid',
            field=django_extensions.db.fields.ShortUUIDField(db_index=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
