# Generated by Django 3.1.6 on 2021-02-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='name',
        ),
    ]