# Generated by Django 2.0.2 on 2018-02-23 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0005_auto_20180221_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rates',
            name='user',
        ),
        migrations.AddField(
            model_name='rates',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]