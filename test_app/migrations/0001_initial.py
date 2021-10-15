# Generated by Django 3.2.7 on 2021-10-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('punishment', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('mark', models.IntegerField()),
                ('limitations', models.CharField(max_length=50)),
                ('plan_file', models.FileField(upload_to='')),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.employer')),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.file')),
            ],
        ),
    ]
