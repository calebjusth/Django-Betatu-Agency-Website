# Generated by Django 4.1.1 on 2022-12-09 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0019_rename_image_user_profile_cv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='about',
            new_name='user_bio',
        ),
        migrations.RenameField(
            model_name='user_profile',
            old_name='CV',
            new_name='user_cv',
        ),
    ]
