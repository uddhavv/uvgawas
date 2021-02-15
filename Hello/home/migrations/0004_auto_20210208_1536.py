# Generated by Django 3.1.4 on 2021-02-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210204_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('start', models.CharField(default=None, max_length=20)),
                ('end', models.CharField(default=None, max_length=20)),
                ('date', models.CharField(default=None, max_length=20)),
                ('Ticket', models.CharField(default=None, max_length=20)),
                ('desc', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Plain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('start', models.CharField(default=None, max_length=20)),
                ('end', models.CharField(default=None, max_length=20)),
                ('date', models.CharField(default=None, max_length=20)),
                ('Ticket', models.CharField(default=None, max_length=20)),
                ('desc', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.CharField(default=None, max_length=50)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('start', models.CharField(default=None, max_length=20)),
                ('end', models.CharField(default=None, max_length=20)),
                ('date', models.CharField(default=None, max_length=20)),
                ('Ticket', models.CharField(default=None, max_length=20)),
                ('desc', models.TextField(default=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='mode',
        ),
    ]