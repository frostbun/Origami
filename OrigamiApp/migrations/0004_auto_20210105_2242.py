# Generated by Django 3.1.4 on 2021-01-05 15:42

import builtins
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OrigamiApp', '0003_auto_20210104_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='user',
            field=models.OneToOneField(on_delete=builtins.any, to=settings.AUTH_USER_MODEL),
        ),
    ]