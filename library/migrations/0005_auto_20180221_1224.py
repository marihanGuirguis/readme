# Generated by Django 2.0.2 on 2018-02-21 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_author_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(default='au.jpg', upload_to=''),
        ),
    ]