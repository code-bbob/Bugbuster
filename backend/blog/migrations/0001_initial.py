# Generated by Django 4.2.5 on 2023-09-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(max_length=44)),
                ('content', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
