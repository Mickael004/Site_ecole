# Generated by Django 5.2 on 2025-05-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMembre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membres',
            name='telephone',
            field=models.CharField(max_length=15),
        ),
    ]
