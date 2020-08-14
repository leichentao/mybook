# Generated by Django 3.0.7 on 2020-08-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=32)),
                ('age', models.CharField(max_length=32)),
                ('sex', models.BooleanField(default=False)),
                ('hobby', models.CharField(max_length=32)),
            ],
        ),
    ]