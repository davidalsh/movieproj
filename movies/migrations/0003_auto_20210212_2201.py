# Generated by Django 3.1.5 on 2021-02-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210210_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=30, verbose_name='Country'),
        ),
    ]
