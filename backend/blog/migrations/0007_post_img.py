# Generated by Django 4.2.6 on 2023-10-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
