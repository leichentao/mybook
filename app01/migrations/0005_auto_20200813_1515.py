# Generated by Django 3.0.7 on 2020-08-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女'), ('secret', '保密')], default='secret', max_length=6),
        ),
    ]
