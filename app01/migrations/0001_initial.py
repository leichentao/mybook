# Generated by Django 3.0.7 on 2020-08-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
                ('petname', models.CharField(max_length=32)),
                ('account', models.CharField(max_length=32)),
            ],
        ),
    ]
