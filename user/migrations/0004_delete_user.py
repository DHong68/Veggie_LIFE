# Generated by Django 2.2.5 on 2022-01-24 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220124_1912'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]