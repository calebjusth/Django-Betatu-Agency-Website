# Generated by Django 4.1.1 on 2022-11-26 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0005_testimonials_alter_userregistration_password1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='testimonials',
            new_name='testimonial',
        ),
    ]