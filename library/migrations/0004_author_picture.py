# Generated by Django 2.0.2 on 2018-02-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20180221_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
