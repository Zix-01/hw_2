# Generated by Django 4.2.2 on 2024-10-29 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]
