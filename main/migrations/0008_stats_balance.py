# Generated by Django 2.2 on 2023-02-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20230206_0608'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
