# Generated by Django 4.2 on 2023-05-03 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("address", "0002_remove_address_user_alter_address_zipcode"),
        ("user", "0003_alter_user_type_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="address.address",
            ),
        ),
    ]