# Generated by Django 3.2.7 on 2021-10-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_auto_20211017_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
