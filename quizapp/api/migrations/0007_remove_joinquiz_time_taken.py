# Generated by Django 3.2.2 on 2021-07-13 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_answers_time_elapsed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinquiz',
            name='time_taken',
        ),
    ]