# Generated by Django 3.2.9 on 2021-11-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.TextField(),
        ),
    ]
