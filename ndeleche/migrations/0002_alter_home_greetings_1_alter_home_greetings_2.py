# Generated by Django 4.2.7 on 2023-11-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndeleche', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=20),
        ),
    ]