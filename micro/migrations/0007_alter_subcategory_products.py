# Generated by Django 4.1.7 on 2023-03-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0006_remove_product_prod_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='products',
            field=models.ManyToManyField(to='micro.product'),
        ),
    ]
