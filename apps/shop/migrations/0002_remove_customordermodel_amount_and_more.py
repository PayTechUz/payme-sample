# Generated by Django 4.2.4 on 2023-08-25 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customordermodel',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='customordermodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customordermodel',
            name='updated_at',
        ),
    ]