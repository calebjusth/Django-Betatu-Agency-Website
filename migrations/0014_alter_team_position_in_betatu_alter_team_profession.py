# Generated by Django 4.1.1 on 2022-11-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0013_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='position_in_betatu',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='profession',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
