# Generated by Django 2.0.2 on 2018-02-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20180223_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='au.jpg', upload_to='library/static/library'),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(upload_to='library/static/library'),
        ),
        migrations.AlterField(
            model_name='category',
            name='pic',
            field=models.ImageField(upload_to='library/static/library'),
        ),
    ]
