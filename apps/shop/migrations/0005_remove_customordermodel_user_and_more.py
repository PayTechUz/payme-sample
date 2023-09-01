# Generated by Django 4.2.4 on 2023-08-27 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customordermodel',
            name='user',
        ),
        migrations.AddField(
            model_name='customordermodel',
            name='phone_number',
            field=models.CharField(default=1, max_length=24),
            preserve_default=False,
        ),
    ]
