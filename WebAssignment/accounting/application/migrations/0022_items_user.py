# Generated by Django 3.0 on 2020-02-06 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.user'),
            preserve_default=False,
        ),
    ]
