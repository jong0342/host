# Generated by Django 3.0.7 on 2022-01-10 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='jong_user',
        ),
    ]
