# Generated by Django 4.1.1 on 2022-11-22 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitatu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
            ],
        ),
    ]