# Generated by Django 4.2 on 2023-05-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type_user',
            field=models.CharField(blank=True, default='client', max_length=20),
        ),
    ]