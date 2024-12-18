# Generated by Django 5.1 on 2024-11-03 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price', 'created_at', 'updated_at', 'category'], 'permissions': [('can_unpublish_product', 'Может отменять публикацию продукта'), ('can_change_product_description', 'Может менять описание продукта'), ('can_change_product_category', 'Может менять категорию продукта')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
