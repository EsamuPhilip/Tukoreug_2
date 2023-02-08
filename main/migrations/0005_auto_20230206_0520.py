# Generated by Django 2.2 on 2023-02-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230203_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='reflink',
            new_name='ref_link',
        ),
        migrations.AddField(
            model_name='user',
            name='ref_code',
            field=models.UUIDField(default=2023),
            preserve_default=False,
        ),
    ]
