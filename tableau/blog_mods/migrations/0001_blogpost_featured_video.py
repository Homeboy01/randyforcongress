# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class AddExtraField(migrations.AddField):

    def __init__(self, *args, **kwargs):
        if 'app_label' in kwargs:
            self.app_label = kwargs.pop('app_label')
        else:
            self.app_label = None
        super(AddExtraField, self).__init__(*args, **kwargs)

    def state_forwards(self, app_label, state):
        super(AddExtraField, self).state_forwards(self.app_label or app_label, state)

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        super(AddExtraField, self).database_forwards(
            self.app_label or app_label, schema_editor, from_state, to_state)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        super(AddExtraField, self).database_backwards(
            self.app_label or app_label, schema_editor, from_state, to_state)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
    ]

    operations = [
        AddExtraField(
            model_name='blogpost',
            name='featured_video',
            field=models.TextField(help_text='Optional, youtube or vimeo iframes here will override featured image above', verbose_name='Featured video', blank=True),
            app_label="blog"
        ),
    ]
