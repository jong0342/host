# Generated by Django 3.0.7 on 2022-01-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='생성일자')),
            ],
        ),
    ]
