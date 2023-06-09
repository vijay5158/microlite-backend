# Generated by Django 4.1.7 on 2023-03-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0002_alter_category_cat_img_alter_product_prod_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(default='', upload_to='static/category/<django.db.models.fields.AutoField>'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(default='', upload_to='static/product/<django.db.models.fields.AutoField>'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_spec',
            field=models.ImageField(default='', upload_to='static/product/<django.db.models.fields.AutoField>'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcat_img',
            field=models.ImageField(default='', upload_to='static/subcategory/<django.db.models.fields.AutoField>'),
        ),
    ]
