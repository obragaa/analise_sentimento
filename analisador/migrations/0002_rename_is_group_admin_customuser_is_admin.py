# Generated by Django 5.0.4 on 2024-04-12 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analisador', '0001_reinit_custom_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_group_admin',
            new_name='is_admin',
        ),
    ]
