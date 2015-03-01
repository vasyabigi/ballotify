# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_auto_20150301_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('user_agent', models.CharField(max_length=255, blank=True)),
                ('ip', models.CharField(max_length=255, blank=True)),
                ('choice', models.ForeignKey(related_name='votes', to='questions.Choice')),
                ('question', models.ForeignKey(related_name='votes', to='questions.Question')),
                ('user', models.ForeignKey(related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
    ]
