# Generated by Django 2.2.5 on 2020-06-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200618_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='통화',
            field=models.CharField(blank=True, choices=[('usd', 'USD$'), ('krw', 'KRW\\')], max_length=7, null=True),
        ),
    ]
