# Generated by Django 3.1.4 on 2021-01-02 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docfile',
        ),
        migrations.RemoveField(
            model_name='document',
            name='email',
        ),
        migrations.RemoveField(
            model_name='document',
            name='message',
        ),
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.RemoveField(
            model_name='document',
            name='phone',
        ),
    ]
