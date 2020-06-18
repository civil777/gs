# Generated by Django 2.2.5 on 2020-06-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200618_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar',
            new_name='프로필사진',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.AddField(
            model_name='user',
            name='성별',
            field=models.CharField(choices=[('male', '남자'), ('female', '여자'), ('other', '기타')], max_length=10, null=True),
        ),
    ]
