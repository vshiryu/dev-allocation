# Generated by Django 5.1.5 on 2025-01-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
