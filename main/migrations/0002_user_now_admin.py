# Generated by Django 2.2 on 2023-02-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='now_admin',
            field=models.BooleanField(default=False),
        ),
    ]
