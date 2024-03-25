# Generated by Django 4.2.6 on 2024-03-22 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_shoppingcart_count_alter_shoppingcart_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='product name'),
        ),
    ]
