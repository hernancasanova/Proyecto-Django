# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animales',
            options={'verbose_name_plural': 'Animales'},
        ),
    ]
