# Generated by Django 2.2.1 on 2019-07-31 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190731_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='query',
        ),
    ]
