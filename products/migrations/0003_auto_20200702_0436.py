# Generated by Django 2.2.5 on 2020-07-01 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200626_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='국가',
            field=django_countries.fields.CountryField(default='KR', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='생산자',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='원산지',
            field=django_countries.fields.CountryField(default='KR', max_length=2),
        ),
    ]
