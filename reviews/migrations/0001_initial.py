# Generated by Django 2.2.5 on 2020-06-26 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('등록한_날짜', models.DateTimeField(auto_now_add=True)),
                ('수정한_날짜', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('품질', models.IntegerField()),
                ('배송', models.IntegerField()),
                ('가격', models.IntegerField()),
                ('신선도', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
