# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_guest_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='image',
        ),
    ]
