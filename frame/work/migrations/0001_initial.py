# Generated by Django 4.0.3 on 2022-03-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('branch', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('phoneno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
