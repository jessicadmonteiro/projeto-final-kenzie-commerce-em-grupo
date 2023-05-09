from django.db import migrations


class Migration(migrations.Migration):

  dependencies = [
        ("products", "0003_product_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="cart",
        ),
    ]
