# Generated by Django 3.2.3 on 2021-05-29 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_message_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
