# Generated by Django 5.0 on 2025-03-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserFacing', '0004_userdownload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
    ]
