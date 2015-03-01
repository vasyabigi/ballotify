# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_choice_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='uuid',
            field=django_extensions.db.fields.ShortUUIDField(db_index=True, max_length=8, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
