# Generated by Django 3.2.7 on 2021-10-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='plan_file',
            field=models.FilePathField(),
        ),
    ]