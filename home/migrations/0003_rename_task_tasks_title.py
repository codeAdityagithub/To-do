# Generated by Django 4.1.3 on 2022-11-14 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tasks_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='task',
            new_name='title',
        ),
    ]
