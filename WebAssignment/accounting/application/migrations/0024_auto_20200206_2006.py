# Generated by Django 3.0 on 2020-02-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0023_vendor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
