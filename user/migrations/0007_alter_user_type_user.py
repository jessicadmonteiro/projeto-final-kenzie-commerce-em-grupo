# Generated by Django 4.2 on 2023-05-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(blank=True, default='cliente', max_length=20),
        ),
    ]
