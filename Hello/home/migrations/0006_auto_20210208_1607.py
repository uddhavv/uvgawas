# Generated by Django 3.1.4 on 2021-02-08 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210208_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='date',
            new_name='Tdate',
        ),
    ]
