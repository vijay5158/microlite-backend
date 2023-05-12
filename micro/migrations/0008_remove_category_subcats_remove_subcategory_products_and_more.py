# Generated by Django 4.1.7 on 2023-03-26 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0007_alter_subcategory_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcats',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='prod_subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='micro.subcategory'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='micro.category'),
        ),
    ]
