# Generated by Django 3.2 on 2022-12-05 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='full_name',
            new_name='user_name',
        ),
    ]
