# Generated by Django 3.0 on 2020-01-10 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20200110_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorials',
            name='iframe_link',
        ),
    ]
