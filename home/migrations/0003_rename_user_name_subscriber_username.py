# Generated by Django 3.2 on 2022-12-05 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_full_name_subscriber_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='user_name',
            new_name='username',
        ),
    ]
