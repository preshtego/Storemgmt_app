# Generated by Django 3.2.5 on 2021-07-25 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0007_stockhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockhistory',
            old_name='timestamp',
            new_name='time',
        ),
    ]
