# Generated by Django 4.2 on 2023-05-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type_user',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
