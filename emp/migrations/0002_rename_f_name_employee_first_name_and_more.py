# Generated by Django 4.2.5 on 2023-11-15 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='l_name',
            new_name='last_name',
        ),
    ]