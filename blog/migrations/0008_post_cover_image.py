# Generated by Django 3.0.5 on 2020-04-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200430_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to='cover_image'),
        ),
    ]