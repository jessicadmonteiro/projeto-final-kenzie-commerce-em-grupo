# Generated by Django 4.2 on 2023-05-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="user",
        ),
        migrations.AlterField(
            model_name="address",
            name="zipcode",
            field=models.IntegerField(),
        ),
    ]
